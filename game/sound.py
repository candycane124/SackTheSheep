import pygame

class Sound():
    def __init__(self, soundName):
        """
        Initialize the Sound class.

        Parameters:
        -----------
        - soundName (str): The name of the sound to be played.
        """
        pygame.mixer.init()
        self.soundVolume = 0.2 #Default sound volume
        #Dictionary mapping sound names to sound files
        self.sounds = {
            'sheep' : pygame.mixer.Sound('assets/sounds/sheep_baa.ogg'),
            'coin': pygame.mixer.Sound('assets/sounds/coin.mp3'),
            'alarm': pygame.mixer.Sound('assets/sounds/alarm.ogg'),
            'alienSmoke' : pygame.mixer.Sound('assets/sounds/Hyper 1.wav'),
            'wolfHit': pygame.mixer.Sound('assets/sounds/dogbark.wav'),
            
        }
        self.soundName = soundName
    def playSound(self):
        """
        Play the specified sound with the set volume.
        """
        self.sounds[self.soundName].set_volume(self.soundVolume) #Set volume for selected sound
        self.sounds[self.soundName].play() #Play selected sound

class Music():
    def __init__(self, musicName):
        """
        Initialize the Music class.

        Parameters:
        -----------
        - musicName (str): The name of the music to be played.
        """
        pygame.mixer.init()
        self.musicVolume = 1 #Set default music volume
        # Dictionary mapping music names to music files
        self.music ={
            'menu': 'assets/sounds/intro track.ogg',
            'level1': 'assets/sounds/backtrack.wav',
            'level2': 'assets/sounds/Meadow Thoughts.ogg',
            'level3': 'assets/sounds/story time.ogg'
         }
        self.musicName = musicName
    def playMusic(self):
        """
        Play the specified music with the set volume.
        """
        music = pygame.mixer.music.load(self.music[self.musicName]) # Load the selected music
        pygame.mixer.music.set_volume(self.musicVolume) # Set the volume for the music
        pygame.mixer.music.play(-1) # Play the music indefinitely (-1 for looping)