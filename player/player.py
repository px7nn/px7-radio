import vlc

class Player:
    def __init__(self):
        self.instance = vlc.Instance('--quiet', "--network-caching=2000")
        self.player = self.instance.media_player_new()
    
    def Play(self, url):
        media = self.instance.media_new(url)
        self.player.set_media(media)
        self.player.play()
    def Pause(self):
        if self.player:
            self.player.pause()
    def Stop(self):
        if self.player:
            self.player.stop()
