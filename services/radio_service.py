import threading, sys, time
import requests as rq
import config

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



def search(params: dict):
    if params.get("name") == None and len(params) == 1:
        return None
    if not params.get("limit"):
        params['limit'] = config.DEFAULT_RADIO_SEARCH_LIMIT
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