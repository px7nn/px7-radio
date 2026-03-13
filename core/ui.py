from . import ping, media_manager
import sys, os, time, threading
from config import HIDE_ERR

done = False

banner = """
        ██████╗ ██╗  ██╗███████╗
        ██╔══██╗╚██╗██╔╝╚════██║
        ██████╔╝ ╚███╔╝     ██╔╝
        ██╔═══╝  ██╔██╗    ██╔╝ 
        ██║     ██╔╝ ██╗   ██║  
        ╚═╝     ╚═╝  ╚═╝   ╚═╝
    - - - - Terminal Radio - - - -
"""

def welcome():
    print(banner)
    media_manager.check_vlc()
    if HIDE_ERR:
        devnull = open(os.devnull, "w")
        sys.stderr = devnull
    connection_status()
    print(f"\nBasic commands:\n\t>> radio search <station name>\n\t>> play <station no.>\n\t>> pause\n\t>> ping\nFor more commands try:\n\t>> help\n")


def connection_status():
    global done
    done = False
    threading.Thread(target=loading, daemon=True).start()
    png = ping.get_ping()
    if png == -1:
        sys.stdout.write("\r\033[KConnection failure: Check your internet")
        sys.stdout.flush()
        done = True
        exit()
    done = True
    time.sleep(0.2)
    print(f"Ping: {png} ms")
    done = False


def loading():
    i = 1
    while not done:
        sys.stdout.write("\r\033[KConnecting" + ". " * (i % 4))
        sys.stdout.flush()
        i+=1
        time.sleep(0.2)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


