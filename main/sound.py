import pygame

class Sound():
    def __init__(self, soundName):
        """
        A class representing a drink item in the menu.
        
        Parameters:
        ----------
        soundName(str): The name of the sound clip
        
        """
        pygame.mixer.init()
        #Default sound volume
        self.soundVolume = 0.2
        #Dictionary mapping sound names to sound files
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
        """
        Play the sound clip specified by soundName.
        """
        self.sounds[self.soundName].set_volume(self.soundVolume)
        self.sounds[self.soundName].play()

class Music():
    def __init__(self, musicName):
        """
        A class representing a music track.
        
        Parameters:
        ----------
        musicName (str): The name of the music track.
        """
        pygame.mixer.init()
        #Default music volume
        self.musicVolume = 0.1
        # Dictionary mapping music names to music files
        self.music ={
            'menu': 'assets/sounds/intro track.ogg',
            'level1': 'assets/sounds/backtrack.wav',
            'level2': 'assets/sounds/Meadow Thoughts.ogg',
            'level3': 'assets/sounds/story time'
         }
        self.musicName = musicName
    def playMusic(self):
        """
        Play the music track specified by musicName on loop.
        """
        music = pygame.mixer.music.load(self.music[self.musicName])
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(-1)