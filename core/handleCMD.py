import requests as rq
from . import ping, media_manager, help
import config
import threading, sys, time

done = False

def preloader():
    i = 1
    while not done:
        sys.stdout.write("\r\033[KSearching" + ". " * (i % 4))
        sys.stdout.flush()
        i+=1
        time.sleep(0.2)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def handle_cmd(cmd: dict):
    if cmd.get('sys') == "ping":
        print(f"pong: {ping.get_ping()} ms")
        return None
    
    elif cmd.get('sys') == "play":
        if not cmd.get('action'):
            print("Command: play <indx>")
            return None
        timeout = int(cmd.get('timeout')) if cmd.get('timeout') else config.DEFAULT_TIMEOUT
        media_manager.play(int(cmd.get('action')) - 1, timeout)
    
    elif cmd.get('sys') == "pause":
        media_manager.pause()
    elif cmd.get('sys') == "resume":
        media_manager.resume()
    elif cmd.get('sys') == "stop":
        media_manager.stop()
    elif cmd.get('sys') == "show":
        cmd.pop('sys')
        if cmd.get('action') == "current" or cmd.get('action') == "cur":
            cmd.pop('action')
            cmd.pop('name')
            media_manager.show_playing(cmd)
        

    elif cmd.get('sys') == "radio":
        cmd.pop('sys')
        if cmd.get('action') == "--help":
            print(help.HELP_PAGE)
            return
        elif cmd.get('action') == "search":
            cmd.pop('action')
            dat = search(cmd)
            if not dat:
                return
            media_manager.show_data(dat)
    
    else:
        print("Unknown command")
        return None

def search(params: dict):
    if params.get("name") == None and len(params) == 1:
        return None
    if not params.get("limit"):
        params['limit'] = config.DEFAULT_SEARCH_LIMIT
    global done
    done = False
    T = threading.Thread(target=preloader, daemon=True)
    T.start()
    try:
        res = rq.get(config.API_URL, params=params, timeout=10)
        if not res.ok:
            print("Server Error")
            return None
        dat = res.json()
        done = True
        T.join()
        print(f"Found: {len(dat)} station(s)\n")
        return dat
    except Exception as e:
        done = True
        T.join()
        print("Error:", e)
        return None
        
