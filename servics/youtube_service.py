import yt_dlp, sys, time, threading
from yt_dlp.utils import DownloadError
from config import YDL_OPTIONS, DEFAULT_YT_SEARCH_LIMIT, DEFAULT_QUERY_POSTFIX

done = True
text = "Connecting"

def preloader():
    i = 1
    while not done:
        sys.stdout.write(f"\r\033[K{text}" + ". " * (i % 4))
        sys.stdout.flush()
        i+=1
        time.sleep(0.2)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def search_yt(query, params: dict):
    global done, text
    done = False
    text = "Connecting"
    T1 = threading.Thread(target=preloader, daemon=True)
    T1.start()
    if not params.get("no-postfix"):
        query += DEFAULT_QUERY_POSTFIX
    limit = params.get("limit") or DEFAULT_YT_SEARCH_LIMIT
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
        done = True
        T1.join()
    except DownloadError as e:
        done = True
        T1.join()
        print("Error: Timed out or Failed to fetch YouTube results:", e)
        return None
    except Exception as e:
        done = True
        T1.join()
        print(
                    f"Error: {e}\n"
                    "Try again. If error persists raise an issue on:\n"
                    "https://github.com/px7nn/px7-radio/issues\n"
                )
        return None
    results = []
    for entry in info["entries"]:
        if not entry:
            continue
        duration = entry.get("duration")
        if not duration:
            continue
        results.append({
            "name": entry.get('title'),
            "url": entry.get("url"),
            "from": entry.get("uploader"),
            "duration": duration,
            "bitrate": "N.A."
        })
    print(f"Found: {len(results)} result(s)\n")
    return results