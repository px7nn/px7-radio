from . import ping

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich import box
import time
import threading

console = Console()
layout = Layout()

WIDTH = 55
NAME = COUNTRY = 'N.A.'



def banner_panel(color="red"):
    return Panel(
    Align.center(f"""[{color}]
        ██████╗ ██╗  ██╗███████╗
        ██╔══██╗╚██╗██╔╝╚════██║
        ██████╔╝ ╚███╔╝     ██╔╝
        ██╔═══╝  ██╔██╗    ██╔╝ 
        ██║     ██╔╝ ██╗   ██║  
        ╚═╝     ╚═╝  ╚═╝   ╚═╝        
    [/{color}]"""), 
    subtitle=f"[{color} bold]Terminal radio[/{color} bold]", width=WIDTH, border_style=f"bold {color}"
    )

def status_panel(status="🔴", name = NAME, country = COUNTRY, color="red"):
    if type(status) != str:
        if int(status) < 100 and int(status) != 1:
            color = "green"
        elif int(status) < 300:
            color = "yellow"
        else:
            color = "red"
        status = f"{status} ms"
    
    return Panel(f"[{color}]Ping: {status}\nNow Playing: {name}\nCountry: {country}[/{color}]", width=WIDTH, border_style=color)

def console_panel(content):
    return Panel(content, width=WIDTH, box=box.MINIMAL, expand=True)


def update_panel():
    global layout
    with Live(layout, refresh_per_second=1, screen=True) as live:
        while True:
            png = ping.get_ping()
            if png == -1:
                layout['banner'].update(banner_panel())
                layout['status'].update(status_panel(status="Connection error | Check your internet"))
            else:
                layout['banner'].update(banner_panel("green"))
                layout['status'].update(status_panel(status=png, color="green"))
            time.sleep(1)


def welcome():
    global layout
    png = ping.get_ping()
    if png == -1:
        console.print("[red]$PX7: Check your internet connection and try again[/red]")
        exit(1)
    layout.split_column(
        Layout(banner_panel("green"), size=10, name="banner"),
        Layout(status_panel(status=png, color="green"), size=5, name="status"),
    )
    T1 = threading.Thread(target=update_panel)
    T1.start()