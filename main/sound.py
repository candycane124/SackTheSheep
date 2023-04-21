import pygame

class Sound:
    def _init_(self, soundName):
        pygame.mixer.init()
        self.soundVolume = 0.2
        self.musicVolume = 0.2
        self.sounds = {
            'sheep' : pygame.mixer.Sound('assets/sounds/sheep_baa.ogg'),
            'coin': pygame.mixer.Sound('assets/sounds/coin.mp3')
        }
        self.soundName = soundName

        # self.music ={
        #     'level1' : pygame.mix
        # }
    def playSound(self):
        self.sounds[self.soundName].set_volume(self.soundVolume)
        self.sounds[self.soundName].play()
    def playMusic(self):
        pass