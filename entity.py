import pygame

class Player():
    '''
    Object that represents the player's character

    Parameters
    -----
    pos : int [ ]
        X & Y position of player
    speed : float
        speed of player
    map : int [ ]
        bounds of player movement
    size : int
        object side length

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
    getMid
        returns x and y position of middle of player
    setPos
        sets player's x and y position
    '''
    def __init__(self, pos, speed, map, size, levelRestrictions=[]) -> None:
        '''
        Parameters
        -----
        pos : int [ ]
            X & Y position of player
        speed : float
            speed of player
        map : int [ ]
            bounds of player movement
        levelRestrictions :
        '''
        self.pos = pos
        self.speed = speed
        self.map = map
        self.levelRestrictions = levelRestrictions
        self.size = size
        pass

    def moveUp(self):
        self.pos[1] -= self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions, self.size):
            self.pos[1] += self.speed

    def moveLeft(self):
        self.pos[0] -= self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions, self.size):
            self.pos[0] += self.speed

    def moveDown(self):
        self.pos[1] += self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions, self.size):
            self.pos[1] -= self.speed

    def moveRight(self):
        self.pos[0] += self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions, self.size):
            self.pos[0] -= self.speed

    def getPos(self):
        return self.pos
    
    def getMid(self):
        return [self.pos[0]+self.size//2,self.pos[1]+self.size//2]
    
    def setPos(self, newPos):
        self.pos = newPos

def checkPos(pos,bounds=[],zones=None,size=30):
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
        if pos[0] >= bounds[0]-size or pos[0] <= 0 or pos[1] >= bounds[1]-size or pos[1] <= 0:
            return True
    # for i in zones:
    #     if pos[0]+size >= i[0] and pos[0] <= i[0]+i[2] and pos[1]+size >= i[1] and pos[1] <= i[1]+i[3]:
    #         return True
    for i in range(len(zones)):
        zones[i] = pygame.Rect(zones[i][0],zones[i][1],zones[i][2],zones[i][3])
    currentRect = pygame.Rect(pos[0], pos[1], size, size)
    for i in zones:
        if i.colliderect(currentRect):
            return True
    return False
    
    
class Sheep():
    '''
    Object that represent's a sheep
    '''
    pass