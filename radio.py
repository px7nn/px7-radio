from api import radio_browser as rb
from ui import ui
from player import Player

def TakeInput(data):
    inp = int(input("Enter Radio No.> "))
    if inp > len(data) or inp <= 0:
        print("Invalid No.")
        return None
    player = Player()
    player.Play(data[inp-1].get('url_resolved'))
    ui.UI_ShowPing()
    ui.UI_ShowSongData(data[inp-1])
    

def main():
    ui.UI_Landing()
    while True:
        ui.UI_Menu()
        inp = int(input("Choice > "))
        if inp == 1:
            qry = input("Name: ")
            data = rb.GetByName(qry)
            if data:
                ui.UI_StationFound(data)
                TakeInput(data)
        elif inp == 2:
            qry = input("Tag: ")
            data = rb.GetByTag(qry)
            if data:
                ui.UI_StationFound(data)
                TakeInput(data)
        elif inp == 3:
            break
main()