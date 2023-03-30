import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *

import entity

#initial game/screen setup
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Sack The Sheep')

#grass
grass= pygame.image.load('SackTheSheep/assets/grass-588.jpg')
grass = pygame.transform.scale(grass, (width, height))

#map
obstacles = [
   [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]
]

#farmer
userSize = 49
userSpeed = 0.3
spawnX = 50
spawnY = 50
farmerImage = pygame.image.load('SackTheSheep/assets/char.png')
farmerImage = pygame.transform.scale(farmerImage, (38, 49))
farmerLeft = farmerImage.copy()
farmerLeft = pygame.transform.flip(farmerLeft, True, False)
user = entity.Player([spawnX,spawnY],userSpeed,[width,height],userSize,obstacles)

#
def reset():
    sheeps = [
       pygame.Rect(100,100,sheepSzX, sheepSzY),pygame.Rect(300,400,sheepSzX, sheepSzY)
    ]
    coins = [
       pygame.Rect(450,350,20,20)
    ]
    return sheeps, coins
#sheep 
sheepSzX = 45
sheepSzY = 35
sheepImage = pygame.image.load('SackTheSheep/assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (sheepSzX, sheepSzY))
#coins
coinImage = pygame.image.load('SackTheSheep/assets/coin.png')
coinImage = pygame.transform.scale(coinImage, (20, 20))
#
sheeps, coins = reset()

score = 0
money = 0
faceRight = True
running = True
while running: 
  #------------
  #INPUT
  #------------
  for event in pygame.event.get():
      if event.type == QUIT:
          #quit game
          pygame.quit()
          sys.exit()
      elif event.type == KEYDOWN:
          #key pressed
          if event.key == K_r:
            #'r' to reset
            user.setPos([spawnX,spawnY])
            score = 0
            money = 0
            sheeps, coins = reset()
          elif event.key == K_ESCAPE:
            #send to pause or menu screen
            pass
  #keyboard input for character movement
  pressed = pygame.key.get_pressed()
  if pressed[K_RIGHT] or pressed[K_d]:
    faceRight = True
    user.moveRight()
  elif pressed[K_LEFT] or pressed[K_a]:
    faceRight = False
    user.moveLeft()
  elif pressed[K_DOWN] or pressed[K_s]:
    user.moveDown()
  elif pressed[K_UP] or pressed[K_w]:
    user.moveUp()

  if not sheeps:
    #you win message
    #send user to success page/choose levels page
    running = False
    print("Level Cleared!")

  #------------
  #OUTPUT
  #------------ 
  #background
  screen.blit(grass, (0,0))
  #sheep
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSize, userSize)
  for s in sheeps:
    screen.blit(sheepImage,(s[0],s[1]))
    #see if sheep have been sacked
    if s.colliderect(farmerRect):
      sheeps.remove(s)
      score +=1
  for i in coins:
    screen.blit(coinImage,(i[0],i[1]))
    if i.colliderect(farmerRect):
       coins.remove(i)
       money += 1
  #obstacles
  for i in obstacles:
    obst = pygame.Rect(i[0],i[1],i[2],i[3])
    pygame.draw.rect(screen,(80,40,10),obst)
  #farmer
  if faceRight:
    screen.blit(farmerImage, (user.getPos()[0],user.getPos()[1]))
  else:
    screen.blit(farmerLeft, (user.getPos()[0],user.getPos()[1]))
  #update display
  pygame.display.update()
