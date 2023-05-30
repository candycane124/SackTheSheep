import pygame

class Animate():
    def __init__(self, key):
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
        self.animationTimer +=1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0 
            self.imageIndex +=1
            if self.imageIndex > len(self.imageList)-1:
                self.imageIndex = 0
    def draw(self,screen,x, y, width, height, flipX, flipY):
        image = self.imageList[self.imageIndex]
        image = pygame.transform.scale(pygame.image.load(image),(width, height))
        image = pygame.transform.flip(image, flipX, flipY)
        screen.blit(image,(x,y))
    def getIndex(self):
        return self.imageIndex
    def resetIndex(self):
        self.imageIndex = 0 



