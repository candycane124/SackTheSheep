import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *

import entity

#game background screen setup
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
obstacles = [[0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]]
#Farmer
userSize = 50
userSpeed = 0.3
defaultPos = [50,50]
farmerImage = pygame.image.load('SackTheSheep/assets/char.png')
farmerImage = pygame.transform.scale(farmerImage, (userSize, userSize))
user = entity.Player(defaultPos,userSpeed,[width,height],userSize,obstacles)

#sheep 
sheepImage = pygame.image.load('SackTheSheep/assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (40, 30))
sheeps = [
  pygame.Rect(100,100,40,30)
]
score = 0

running = True
while running: 
  #------------
  #INPUT
  #------------
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  pressed = pygame.key.get_pressed()
  if pressed[K_RIGHT] or pressed[K_d]:
    user.moveRight()
  elif pressed[K_LEFT] or pressed[K_a]:
    user.moveLeft()
  elif pressed[K_DOWN] or pressed[K_s]:
    user.moveDown()
  elif pressed[K_UP] or pressed[K_w]:
    user.moveUp()
  elif pressed[K_r]:
    user.setPos(defaultPos)
  
  #background
  screen.blit(grass, (0,0))
  #see if sheep have been sacked
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSize, userSize)
  for s in sheeps:
    screen.blit(sheepImage,(s[0],s[1]))
    if s.colliderect(farmerRect):
      sheeps.remove(s)
      score +=1
  #obstacles
  for i in obstacles:
    obst = pygame.Rect(i[0],i[1],i[2],i[3])
    pygame.draw.rect(screen,(80,40,10),obst)
  #farmer
  screen.blit(farmerImage, (user.getPos()[0],user.getPos()[1]))
  
  pygame.display.update()
  