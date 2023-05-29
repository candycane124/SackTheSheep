import pygame, sys
from pygame.locals import *

def genText(screen, txt, colour, pos, posType, size=16):
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
  font = pygame.font.SysFont("monospace", size)
  # font = pygame.font.Font('freesansbold.ttf', size)
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

def highScore(controller):
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('STS High Scores')

    highScores = []

    files = ["game/scores/lvl1.txt","game/scores/lvl2.txt","game/scores/lvl3.txt"]
    for f in files:
        currentScores = []
        with open(f,"r") as textFile:
            info = textFile.readlines()
            scores = info[0].split()
            names = info[1].split()
        for i in range(3):
            currentScores.append(f"{scores[i]} {names[i]}")
        highScores.append(currentScores)

    background = pygame.transform.scale(pygame.image.load("assets/background.jpg"),(896,504))

    white = (250,250,250)
    gray = (20,100,20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                #quit game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                controller.normalWindow("LevelSelect")
                return
        # screen.fill((180,180,180))
        screen.blit(background,(-100,0))
        pygame.draw.rect(screen,gray,(15,80,150,350))
        pygame.draw.rect(screen,gray,(175,80,150,350))
        pygame.draw.rect(screen,gray,(335,80,150,350))
        genText(screen,"Level 1",white,(115,90),"middle",20)
        genText(screen,"Level 2",white,(115,250),"middle",20)
        genText(screen,"Level 3",white,(115,410),"middle",20)
        for i in highScores:
           for j in i:
              genText(screen,j.split()[0],white,(150+50*i.index(j),30+160*highScores.index(i)),"top-left")
              genText(screen,j.split()[1],white,(150+50*i.index(j),150+160*highScores.index(i)),"top-right")
        pygame.display.update()


# highScore()