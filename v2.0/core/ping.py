import requests
import time

def get_ping(URL = "https://www.google.com") -> int:
    try:
        strt = time.time()
        requests.get(URL, timeout=3)
        return int((time.time() - strt) * 1000)
    except:
        return -1
