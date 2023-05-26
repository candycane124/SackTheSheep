import pygame, sys
from pygame.locals import *

def genText(screen, txt, colour, pos, posType, size=14):
  '''
  Blit's text to screen
  Parameters
  -----
  screen : str
    Surface for text to be displayed on
  txt : Str
    Text that will be displayed
  colour : int ( )
    RGB colour of text
  pos : int [ ]
    y, x position of text
  posType : Str
    "top-right", "bottom-left", "bottom-right", "top-left", or "middle"
  '''
  font = pygame.font.Font('freesansbold.ttf', size)
  rendered = font.render(txt, True, colour)
  rendRect = rendered.get_rect()
  if posType == "top-right":
    rendRect.top = pos[0]
    rendRect.right = pos[1]
  elif posType == "bottom-left":
    rendRect.bottom = pos[0]
    rendRect.left = pos[1]
  elif posType == "bottom-right":
    rendRect.bottom = pos[0]
    rendRect.right = pos[1]
  elif posType == "top-left":
    rendRect.top = pos[0]
    rendRect.left = pos[1]
  elif posType == "middle":
    rendRect.center = (pos[1], pos[0])
  screen.blit(rendered,rendRect)

def highScore():
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('STS High Scores')

    scores = []

    files = ["game/scores/lvl1.txt","game/scores/lvl2.txt","game/scores/lvl3.txt"]
    for f in files:
        currentScores = []
        with open(f,"r") as textFile:
            info = textFile.readlines()
            scores = info[0].split()
            names = info[1].split()
        for i in names:
            currentScores.append(f"{scores[names.index(i)]} {i}")
        scores.append(currentScores)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                #quit game
                pygame.quit()
                sys.exit()
        screen.fill((180,180,180))
        for level in range(len(scores)):
            genText(screen,"LEVEL " + str(level),(20,20,20),(50,100+100*level),"middle")
            for score in scores[level]:
                genText(screen,score,(20,20,20),(50+50*scores[level].index(score),100+10*level),"middle",10)
        pygame.display.update()


highScore()