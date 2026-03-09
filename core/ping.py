from ping3 import ping

def get_ping(HOST = "www.google.com") -> int:
    try:
        res = ping(HOST, timeout=3, unit="ms")
        if res is None or res is False:
            return -1
        return int(res)
    except Exception:
        return -1
