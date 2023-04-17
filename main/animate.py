import pygame

class Animate():
    def __init__(self, imageList):
        self.imageList = imageList
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 8
    def update(self):
        self.animationTimer +=1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0 
            self.imageIndex +=1
            if self.imageIndex > len(self.imageList)-1:
                self.imageIndex = 0
    def draw(self,screen, x, y):
        screen.blit(self.imageList[self.imageIndex],(x,y))
    def getIndex(self):
        return self.imageIndex
    def resetIndex(self):
        self.imageIndex = 0 



