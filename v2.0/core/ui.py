from . import ping
import time
import sys
import threading

print_lock = threading.Lock()
def welcome():
    print("\n===========================")
    print("||   PX7 Terminal Radio  ||")
    print("===========================\n")

def print_error_connection():
    with print_lock:
        sys.stdout.write("\033[s")
        sys.stdout.write("\033[7;1H⚠ Connection Error: Check your internet Connection\033[K")
        sys.stdout.write("\033[u")
    
connection_lost = False
def print_network_status(once = False):
    global connection_lost

    if once:
        PING = ping.get_ping()
        if PING == -1:
            print_error_connection()
            connection_lost = True
            return -1
        elif PING < 100:
            status = "🟢 GOOD"
        elif PING < 300:
            status = "🟡 SLOW"
        elif PING >= 300:
            status = "🔴 POOR"   

        with print_lock:
            sys.stdout.write("\033[s")
            sys.stdout.write(f"\033[7;1HNETWORK STATUS: {status} | {PING} ms\033[K")
            sys.stdout.write(f"\033[8;1H---------------------------------\033[K")
            sys.stdout.write("\033[u")
        return 0
    while True:
        PING = ping.get_ping()
        if PING == -1:
            print_error_connection()
            connection_lost = True
            return -1
        elif PING < 100:
            status = "🟢 GOOD"
        elif PING < 300:
            status = "🟡 SLOW"
        elif PING >= 300:
            status = "🔴 POOR"

        with print_lock:
            sys.stdout.write("\033[s")
            sys.stdout.write(f"\033[7;1HNETWORK STATUS: {status} | {PING} ms\033[K")
            sys.stdout.write(f"\033[8;1H---------------------------------\033[K")
            sys.stdout.write("\033[u")
        time.sleep(5)

def print_help():
    with print_lock:
        print("\n\nCommands: ")
        print("\t>> radio search <name>")
        print("\t>> radio search --tag <tag>")
        print("\t>> exit\n")