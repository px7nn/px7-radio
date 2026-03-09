import requests as rq
from . import ping

def handle_cmd(cmd: dict):
    if cmd.get('action') == "ping":
        print(f"pong: {ping.get_ping()} ms")
        return None

    elif cmd.get('action') == "search":
        cmd.pop('action')
        return search(cmd)
    
    else:
        print("Unknown command")
        return None

def search(params: dict):
    try:
        url = "https://de1.api.radio-browser.info/json/stations/search"
        res = rq.get(url, params=params, timeout=5)
        if not res.ok:
            print("Server Error")
            return None
        return res.json()
    except:
        print("Timeout error")
        return None