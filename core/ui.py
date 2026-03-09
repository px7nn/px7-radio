from . import ping
import sys
import time
import threading

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
    connection_status()
    print(f"\nUseful commands:\n\t>> radio search <name>\n\t>> radio search --tag=TAGNAME --limit=10\n\t>> radio --help\n")


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


