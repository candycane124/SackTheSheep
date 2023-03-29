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
    size

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
        if checkPos(self.pos, self.map, self.levelRestrictions):
            self.pos[1] += self.speed

    def moveLeft(self):
        self.pos[0] -= self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions):
            self.pos[0] += self.speed

    def moveDown(self):
        self.pos[1] += self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions):
            self.pos[1] -= self.speed

    def moveRight(self):
        self.pos[0] += self.speed
        if checkPos(self.pos, self.map, self.levelRestrictions):
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
        rectangle side length, default 20

    Returns
    -----
    boolean
        if position is outside of bounds
    '''
    if bounds != []:
        if pos[0] >= bounds[0]-size or pos[0] <= 0 or pos[1] >= bounds[1]-size or pos[1] <= 0:
            return True
    for i in zones:
        if pos[0]+size >= i[0] and pos[0] <= i[0]+i[2] and pos[1]+size >= i[1] and pos[1] <= i[1]+i[3]:
            return True
    return False
    
    
class Sheep():
    '''
    Object that represent's a sheep
    
    Parameters
    -----
    pos : int [ ]
        the x and y position of the sheep
    claimed : boolean
        if the sheep has been caught, deafult False
    '''
    def __init__(self,pos,claimed=False) -> None:
        self.pos = pos
        self.claimed = claimed
        pass

    def getPos(self):
        return self.pos
    
    def claim(self, pos):
        xDiff = abs(self.pos[0]-pos[0])
        yDiff = abs(self.pos[1]-pos[1])
        if xDiff <= 15 and yDiff <= 15:
            self.claimed = True

    def getState(self):
        return self.claimed