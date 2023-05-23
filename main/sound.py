import pygame

class Sound():
    def __init__(self, soundName):
        pygame.mixer.init()
        self.soundVolume = 0.2
        self.sounds = {
            'sheep' : pygame.mixer.Sound('assets/sounds/sheep_baa.ogg'),
            'coin': pygame.mixer.Sound('assets/sounds/coin.mp3'),
            'alarm': pygame.mixer.Sound('assets/sounds/alarm.ogg'),
            'alienSmoke' : pygame.mixer.Sound('assets/sounds/Hyper 1.wav'),
            'wolfHit': pygame.mixer.Sound('assets/sounds/dogbark.wav'),
            'win': pygame.mixer.Sound('assets/sounds/Win sound.wav'),
            'lose': pygame.mixer.Sound('assets/sounds/gameover.wav')
            
        }
        self.soundName = soundName
    def playSound(self):
        self.sounds[self.soundName].set_volume(self.soundVolume)
        self.sounds[self.soundName].play()

class Music():
    def __init__(self, musicName):
        pygame.mixer.init()
        self.musicVolume = 0.1
        self.music ={
            'menu': 'assets/sounds/intro track.ogg',
            'level1': 'assets/sounds/backtrack.wav',
            'level2': 'assets/sounds/Meadow Thoughts.ogg',
            'level3': 'assets/sounds/story time'
         }
        self.musicName = musicName
    def playMusic(self):
        music = pygame.mixer.music.load(self.music[self.musicName])
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(-1)