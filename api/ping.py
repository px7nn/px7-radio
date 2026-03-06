import requests as rq
import time
from . import PING_URL

def GetPing(url = PING_URL):
    try:
        start = time.time()
        res = rq.get(url, timeout=3)
        ping = (time.time() - start) * 1000
        if ping < 100:
            status = "🟢 GOOD"
        elif ping < 300:
            status = "🟡 SLOW"
        else:
            status = "🔴 BAD"
        return { 
            'ping': f"{ping:.2f} ms", 
            'status': status
        }
    except:
        return {
            'ping': None,
            'status': "🔴 No Internet Connection"
        }
