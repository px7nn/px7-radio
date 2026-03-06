import sys
import threading
from core import ping, ui

args = sys.argv

def safe_input(prompt = ""):
    with ui.print_lock:
        sys.stdout.write(prompt)
    return input()

def main():
    ui.welcome()
    if ui.print_network_status(once=True) == -1:
        exit()
    T1 = threading.Thread(target=ui.print_network_status, daemon=True)
    T1.start()
    ui.print_help()
    while True:
        if ui.connection_lost:
            exit()
        cmd = safe_input(">> ")
        
main()