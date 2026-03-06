from api import ping

def UI_Landing():
    print("\n  PX7 Terminal Radio")
    UI_ShowPing()
    print("----------------------")

def UI_StationFound(data):
    print(len(data), "stations found\n")
    for indx, i in enumerate(data):
        print(f"{indx+1:2}. {i.get('name')[:48]:<60} | {i.get('country')}")
    print()

def UI_Menu():
    print("1. Search By Name\n2. Search By Tag\n3. Exit\n")

def UI_ShowPing():
        pingD = ping.GetPing()
        print(f"Connection: {pingD['status']} | {pingD['ping']}\n")
        pingD = ping.GetPing()

def UI_ShowSongData(song):
    print(f"Now Playing: {song.get("name")}\nCountry: {song.get("country")}")