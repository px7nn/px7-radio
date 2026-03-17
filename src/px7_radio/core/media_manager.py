import sys, threading, time
from px7_radio.services import youtube_service as ys

def check_vlc():
    try:
        import vlc
        vlc.Instance()
    except Exception:
        print("Error: VLC Media Player is not installed or not found in system PATH.")
        print("-" * 50)
        if sys.platform.startswith('win'):
            print("Download Windows version: https://www.videolan.org")
        elif sys.platform.startswith('darwin'):
            print("Download macOS version: https://www.videolan.org")
        else:
            print("Install via your package manager (e.g., sudo apt install vlc)")
        print("-" * 50)
        sys.exit(1)
    return vlc

vlc = check_vlc()

class Player:
    def __init__(self):
        self.Instance = vlc.Instance("--quiet --no-xlib --log-verbose=0 --no-video")
        self.Player = self.Instance.media_player_new()
    def play(self, url):
        self.stop()
        media = self.Instance.media_new(url)
        self.Player.set_media(media)
        self.Player.play()
    def pause(self):
        self.Player.pause()
    def resume(self):
        self.Player.play()
    def stop(self):
        self.Player.stop()

    def get_player(self):
        return self.Player

data = []
index = None
src = ""
done = True
text = ""
player = Player()

def preloader():
    i = 1
    while not done:
        sys.stdout.write(f"\r\033[K{text}" + ". " * (i % 4))
        sys.stdout.flush()
        i+=1
        time.sleep(0.2)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def extract_data(dat: list):
    global data
    data = []
    for d in dat:
        station = {
            "name": d.get("name")[:35].strip(),
            "from": d.get("country"),
            "bitrate": d.get("bitrate") if d.get("bitrate") != 0 else "N.A.",
            "url": d.get("url_resolved")
        }
        data.append(station)

def show_data(dat: list):
    global src
    src = "radio"
    extract_data(dat)
    if len(data) == 0:
        return None
    print(f"{'No.':<4} {'Station name':<40} {'Bitrate':<8}")
    for i, station in enumerate(data, 1):
        print(f"{i:<4} {station.get('name'):<40} {station.get('bitrate'):<8}")
    print()

def show_data_yt(dat: list):
    global data, src
    src = "yt"
    data = dat
    if len(dat) == 0:
        return None
    print(f"{'No.':<4} {'Title':<40}")
    for i, source in enumerate(data, 1):
        print(f"{i:<4} {source.get('name'):<40}")
    print()

def play(indx, timeout):
    length = len(data)
    if length == 0:
        print("Error: List Empty:\nSearch something first.")
        return None
    if indx < 0 or indx >= length:
        print("Error: Index Not in Range. . .")
        return None
    global text, done, index
    done = False
    text = "Checking stream URL"
    T1 = threading.Thread(target=preloader, daemon=True)
    T1.start()
    if not data[indx].get("url") and src=="yt":
        text = "Collecting stream URL"
        url = ys.get_stream_url(data[indx].get("video_url"))
        if not url:
            done = True
            T1.join()
            print("Error: Stream URL not found.")
            return None
        data[indx]["url"] = url
    index = indx
    text = "Loading"
    player.play(data[indx].get("url"))
    while True:
        time.sleep(0.2)
        timeout-=0.2
        if player.get_player().is_playing():
            text = "Playing"   
        else:
            text = "Buffering"
        if timeout <= 0:
            break
    done = True
    T1.join()
    if player.get_player().is_playing():
        print("Now Playing:", data[indx].get("name"))
    else:
        stop()
        print(
            "Stream failed to respond.\n"
            "Possible causes: slow network.\n"
            "Tip: try another stream or increase timeout (>> play <index> --timeout=10)."
        )

def pause():
    player.pause()
    print("Player paused")

def resume():
    player.resume()
    print("Player resumed")

def stop():
    player.stop()

def show_playing(params: dict, expose=False):
    if not data or index == None:
        print("Error: List Empty:\nUse after:\n\t>> radio search <name>\n\t>> play <index>")
        return
    if not params:
        print(f"Title: {data[index].get('name')}")
        print(f"From: {data[index].get('from')}")
        print(f"Bitrate: {data[index].get('bitrate')}")
        if expose:
            print(f"URL: {data[index].get('url')}")
        return
    if params.get("expose"):
        params.pop('expose')
        show_playing({}, True)