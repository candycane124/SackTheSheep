import pygame

class Animate():
    def __init__(self, key):
        """
    Initializes an instance of the Animate class.

    Parameters:
    ----------
    - key (str): The key to access the image dictionary for a specific animation.

    Attributes:
    -----------
    - imageDict (dict): A dictionary containing animation keys and corresponding image paths.
    - key (str): The key to access the desired animation from the image dictionary.
    - imageList (list): A list of image paths for the current animation.
    - imageIndex (int): The index of the current image being displayed.
    - animationTimer (int): A counter to control the timing of the animation.
    - animationSpeed (int): The speed at which the animation should play.
    """
        self.imageDict = {
            'wolfF':['assets/wolfForward/wolfFront1.png',
                     'assets/wolfForward/wolfFront2.png',
                     'assets/wolfForward/wolfFront3.png',
                     'assets/wolfForward/wolfFront4.png',
                     'assets/wolfForward/wolfFront5.png',
                     'assets/wolfForward/wolfFront6.png',
                     'assets/wolfForward/wolfFront7.png',
                     ],
            'wolfB':['assets/wolfBack/wolfBack1.png',
                     'assets/wolfBack/wolfBack2.png',
                     'assets/wolfBack/wolfBack3.png',
                     'assets/wolfBack/wolfBack4.png',
                     'assets/wolfBack/wolfBack5.png',
                     'assets/wolfBack/wolfBack6.png',
                     'assets/wolfBack/wolfBack7.png',
                     ],
            'wolfR':['assets/wolfRunRight/wolfFrame1.png',
                     'assets/wolfRunRight/wolfFrame2.png',
                     'assets/wolfRunRight/wolfFrame3.png',
                     'assets/wolfRunRight/wolfFrame4.png',
                     'assets/wolfRunRight/wolfFrame5.png',
                     'assets/wolfRunRight/wolfFrame6.png',
                    ],
            'farmRun':['assets/farmerRun/Hobbit - run1.png',
                       'assets/farmerRun/Hobbit - run2.png',
                       'assets/farmerRun/Hobbit - run3.png',
                       'assets/farmerRun/Hobbit - run4.png',
                       'assets/farmerRun/Hobbit - run5.png',
                       'assets/farmerRun/Hobbit - run7.png',
                       'assets/farmerRun/Hobbit - run8.png',
                       'assets/farmerRun/Hobbit - run9.png',
                       'assets/farmerRun/Hobbit - run10.png'
            
            ],
            'farmDie':['assets/farmerDie/Hobbit - death1.png',
                       'assets/farmerDie/Hobbit - death2.png',
                       'assets/farmerDie/Hobbit - death3.png',
                       'assets/farmerDie/Hobbit - death4.png',
                       'assets/farmerDie/Hobbit - death5.png',
                       'assets/farmerDie/Hobbit - death6.png',
                       'assets/farmerDie/Hobbit - death7.png',
                       'assets/farmerDie/Hobbit - death8.png',
                       'assets/farmerDie/Hobbit - death9.png',
                       'assets/farmerDie/Hobbit - death10.png',
                       'assets/farmerDie/Hobbit - death11.png',
                       'assets/farmerDie/Hobbit - death12.png',
            ],
            'farmStop':['assets/farmerStop/Hobbit - Idle1.png',
                        'assets/farmerStop/Hobbit - Idle2.png',
                        'assets/farmerStop/Hobbit - Idle3.png',
                        'assets/farmerStop/Hobbit - Idle4.png',
            
            ],
            'coin':['assets/coinAnimate/sprite_0.png',
                    'assets/coinAnimate/sprite_1.png',
                    'assets/coinAnimate/sprite_1.png',
                    'assets/coinAnimate/sprite_2.png',
                    'assets/coinAnimate/sprite_2.png',
                    'assets/coinAnimate/sprite_3.png',
                    'assets/coinAnimate/sprite_3.png',
                    'assets/coinAnimate/sprite_3.png',
                    'assets/coinAnimate/sprite_4.png',
                    'assets/coinAnimate/sprite_4.png',
                    'assets/coinAnimate/sprite_5.png',
                    'assets/coinAnimate/sprite_5.png',
                    'assets/coinAnimate/sprite_6.png',
                    'assets/coinAnimate/sprite_6.png',
                    'assets/coinAnimate/sprite_7.png',
                    'assets/coinAnimate/sprite_7.png',
                    'assets/coinAnimate/sprite_8.png',
                    'assets/coinAnimate/sprite_8.png',
            ],

            'smoke':['assets/smokeAnimation/FX001_01.png',
                     'assets/smokeAnimation/FX001_01.png',
                     'assets/smokeAnimation/FX001_02.png',
                     'assets/smokeAnimation/FX001_02.png',
                     'assets/smokeAnimation/FX001_03.png',
                     'assets/smokeAnimation/FX001_03.png',
                     'assets/smokeAnimation/FX001_04.png',
                     'assets/smokeAnimation/FX001_04.png',
                     'assets/smokeAnimation/FX001_05.png',
                     'assets/smokeAnimation/FX001_05.png'
            ]
        }
        self.key = key
        self.imageList = self.imageDict[self.key]
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 40 #slightly adjusted for Snow's laptop (initial was 10)
    def update(self):
        """
        Updates the animation state.

        Increments the animation timer and updates the image index
        to display the next image in the animation sequence. If the end of the
        sequence is reached, it wraps around to the beginning.
        """
        self.animationTimer +=1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0 
            self.imageIndex +=1
            if self.imageIndex > len(self.imageList)-1:
                self.imageIndex = 0
    def draw(self,screen,x, y, width, height, flipX, flipY):
        """
        Draws the current image of the animation on the screen.

        Parameters:
        -----------
        - screen (pygame.Surface): The surface to draw the image on.
        - x (int): The x-coordinate of the top-left corner of the image.
        - y (int): The y-coordinate of the top-left corner of the image.
        - width (int): The width of the image.
        - height (int): The height of the image.
        - flipX (bool): Whether to flip the image horizontally.
        - flipY (bool): Whether to flip the image vertically.
        """
        image = self.imageList[self.imageIndex]
        image = pygame.transform.scale(pygame.image.load(image),(width, height))
        image = pygame.transform.flip(image, flipX, flipY)
        screen.blit(image,(x,y))
    def getIndex(self):
        """
        Returns the index of the current image being displayed.

        Returns:
        - imageIndex (int): The index of the current image.
        """
        return self.imageIndex
    def resetIndex(self):
        """
        Resets the image index to the beginning of the animation sequence.
        """
        self.imageIndex = 0 



