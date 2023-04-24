import pygame

class Level:
    def _init_(self, win = None, lose = None):
        self.win = win
        self.lose = lose
    def isWon(self):
        if self.win == None:
            return False
        return self.win(self)
    def isLost(self):
        if self.lose == None:
            return False
        return self.lose(self)

def lostLevel(level):
    