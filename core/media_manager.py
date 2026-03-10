import vlc, sys, threading, time

class Player:
    def __init__(self):
        self.Instance = vlc.Instance('-q')
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
index = 0
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
    global data, done
    data = []
    for d in dat:
        station = {
            "name": d.get("name")[:40].strip(),
            "country": d.get("country"),
            "bitrate": d.get("bitrate"),
            "url": d.get("url_resolved")
        }
        data.append(station)

def show_data(dat: list):
    extract_data(dat)
    length = len(data)
    if length == 0:
        return None
    print("No.\t Station name")
    for i in range(length):
        print(f"{i+1}\t {data[i].get("name")}")

def play(indx):
    length = len(data)
    if length == 0:
        print("Error: List Empty:\nUse after >> radio search <name>")
        return None
    if indx < 0 or indx >= length:
        print("Error: Index Not in Range. . .")
        return None
    global done, text, index
    index = indx
    done = False
    text = "Connecting"
    T1 = threading.Thread(target=preloader, daemon=True)
    T1.start()
    
    player.play(data[indx].get("url"))
    text = "Connecting"
    timeout = 5
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
        print("Playing")
        now_playing()
    else:
        stop()
        print("Poor network quality")

def pause():
    player.pause()
    print("Player paused")

def resume():
    player.resume()
    print("Player resumed")

def stop():
    player.stop()

def now_playing():
    print(f"Now: {data[index].get("name")}\nCountry: {data[index].get("country")}\n")