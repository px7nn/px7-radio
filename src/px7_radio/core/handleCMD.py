from . import ping, media_manager, help
from px7_radio.services import radio_service as rs
from px7_radio.services import youtube_service as ys
import px7_radio.config as config

def handle_cmd(cmd: dict):
    if cmd.get('sys') == "ping":
        print(f"pong: {ping.get_ping()} ms")
        return None
    
    elif cmd.get('sys') == "--help" or cmd.get('sys') == "help":
        print(help.HELP_PAGE)
        return
    
    elif cmd.get('sys') == "yt":
        cmd.pop('sys')
        if cmd.get('action') == "search":
            cmd.pop('action')
            if not cmd.get("name"):
                print("Error: Empty query. USAGE:\n\t>> yt search <query>")
                return
            dat = ys.search_yt(cmd.pop("name"), cmd)
            if not dat:
                return
            media_manager.show_data_yt(dat)
    
    elif cmd.get('sys') == "play":
        if not cmd.get('action'):
            print("Command: play <indx>")
            return None
        timeout = int(cmd.get('timeout')) if cmd.get('timeout') else config.DEFAULT_TIMEOUT
        media_manager.play(int(cmd.get('action')) - 1, timeout)
    
    elif cmd.get('sys') == "pause":
        media_manager.pause()
    elif cmd.get('sys') == "resume":
        media_manager.resume()
    elif cmd.get('sys') == "stop":
        media_manager.stop()
    elif cmd.get('sys') == "show":
        cmd.pop('sys')
        if cmd.get('action') == "current" or cmd.get('action') == "cur":
            cmd.pop('action')
            cmd.pop('name')
            media_manager.show_playing(cmd)
        

    elif cmd.get('sys') == "radio":
        cmd.pop('sys')
        # if cmd.get('action') == "--help":
        #     print(help.HELP_PAGE)
        #     return
        if cmd.get('action') == "search":
            cmd.pop('action')
            dat = rs.search(cmd)
            if not dat:
                return
            media_manager.show_data(dat)
    
    else:
        print("Unknown command")
        return None