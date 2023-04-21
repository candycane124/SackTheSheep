import pygame

class Player():
    '''
    Object that represents the player's character

    Parameters
    -----
    pos : float [ ]
        X & Y position of player
    speed : float
        speed of player
    map : int [ ]
        main bounds of player movement
    sizeX : int
        object x side length
    sizeY : int
        object y side length
    levelRestrictions : int [x1, y1, width, height, imgId] [ ]
        list of areas the player can not go
    Methods
    -----
    moveUp
        attempts to decreases Y co-ordinate by player speed
    moveLeft
        attempts to decreases X co-ordinate by player speed
    moveDown
        attempts to increases Y co-ordinate by player speed
    moveRight
        attempts to increases X co-ordinate by player speed
    getPos
        returns current position
    setPos
        sets player's x and y position
    '''
    def __init__(self, pos, speed, map, sizeX, sizeY, health, imgs, levelRestrictions=[]) -> None:
        '''
        Parameters
        -----
        pos : int [ ]
            X & Y position of player
        speed : float
            speed of player
        map : int [ ]
            bounds of player movement
        imgs : 

        levelRestrictions :
        '''
        self.pos = pos
        self.speed = speed
        self.map = map
        self.health = health
        self.imgs = imgs
        self.levelRestrictions = levelRestrictions
        self.sizeX = sizeX
        self.sizeY = sizeY
        pass

    def moveUp(self):
        self.pos[1] -= self.speed
        if checkPos(self.pos, self.sizeX, self.sizeY, self.imgs, self.map, self.levelRestrictions):
            self.pos[1] += self.speed

    def moveLeft(self):
        self.pos[0] -= self.speed
        if checkPos(self.pos, self.sizeX, self.sizeY, self.imgs, self.map, self.levelRestrictions):
            self.pos[0] += self.speed

    def moveDown(self):
        self.pos[1] += self.speed
        if checkPos(self.pos, self.sizeX, self.sizeY, self.imgs, self.map, self.levelRestrictions):
            self.pos[1] -= self.speed

    def moveRight(self):
        self.pos[0] += self.speed
        if checkPos(self.pos, self.sizeX, self.sizeY, self.imgs, self.map, self.levelRestrictions):
            self.pos[0] -= self.speed

    def getPos(self):
        return self.pos
    
    def setPos(self, newPos):
        self.pos = newPos

    def setSpeed(self, newSpeed):
        self.speed = newSpeed
    
    def changeHealth(self, newHealth=False):
        '''
        newHealth : int [ ]
            new health of player, leave empty to decrease health by one
        '''
        if newHealth:
            self.health = newHealth[0]
        else:
            self.health -= 1
        pass
    
    def getHealth(self):
        return self.health
        

# def returnRect(x):
#     return pygame.Rect(x[0],x[1],x[2],x[3])
    
# def checkCollision(x,y):
#     for i in y:
#         if x.pygame.Rect.colliderect(i):
#             return True
#     return False

def checkPos(pos,sizeX,sizeY,imgs,bounds=[],zones=None):
    '''
    Checks if current position is outside of bounds
    
    Parameters
    -----
    pos : int [ ]
        current x and y position


    bounds : int [ ]
        max x and y boundaries
    zones : int [x1, y1, width, height] [ ]
        restricted areas
    size : int
        rectangle side length, default 30

    Returns
    -----
    boolean
        if position is outside of bounds
    '''
    if bounds != []:
        if pos[0] >= bounds[0]-sizeX or pos[0] <= 0 or pos[1] >= bounds[1]-sizeY or pos[1] <= 0:
            return True
    charMask = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets/farmerRun/Hobbit - run7.png"),(38,38)))
    obstacles = zones.copy()
    # for i in range(len(obstacles)):
    #     obstacles[i] = pygame.Rect(obstacles[i][0],obstacles[i][1],obstacles[i][2],obstacles[i][3])
    # currentRect = pygame.Rect(pos[0], pos[1], sizeX, sizeY)
    for i in obstacles:
        obstMask = pygame.mask.from_surface(imgs[i[4]])
        if charMask.overlap(obstMask,(i[0]-pos[0],i[1]-pos[1])):
            return True
    return False
    
    
class Sheep():
    '''
    Object that represent's a sheep
    '''
    pass