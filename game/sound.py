import pygame

class Sound():
    def __init__(self, soundName):
        pygame.mixer.init()
        self.soundVolume = 0.2
        self.sounds = {
            'sheep' : pygame.mixer.Sound('assets/sounds/sheep_baa.ogg'),
            'coin': pygame.mixer.Sound('assets/sounds/coin.mp3'),
            'alarm': pygame.mixer.Sound('assets/sounds/alarm.ogg'),
            'alienSmoke' : pygame.mixer.Sound('assets/sounds/Hyper 1.wav')
        }
        self.soundName = soundName
    def playSound(self):
        self.sounds[self.soundName].set_volume(self.soundVolume)
        self.sounds[self.soundName].play()

class Music():
    def __init__(self, musicName):
        pygame.mixer.init()
        self.musicVolume = 1
        self.music ={
            'level1': 'assets/sounds/backtrack.wav',
            'level3': 'assets/sounds/alientrack.wav'
         }
        self.musicName = musicName
    def playMusic(self):
        music = pygame.mixer.music.load(self.music[self.musicName])
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(-1)