import pygame, sys
from pygame.locals import QUIT
#game background screen setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Sack The Sheep')
#grass
grass= pygame.image.load('grass.png')
grass = pygame.transform.scale(grass, (500, 500))

#Farmer
farmerImage = pygame.image.load('farmer.png')
farmerImage = pygame.transform.scale(farmerImage, (50, 50))
farmerX = 0
farmerY= 0

#sheep 
sheepImage = pygame.image.load('sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (40, 30))
sheeps = [
  pygame.Rect(100,100,40,30)
]
score = 0

while True: 
  #------------
  #INPUT
  #------------
  
  #check if quit
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  newFarmerX = farmerX
  newFarmerY = farmerY
  #player input
  keys = pygame.key.get_pressed()
  #a-left
  if keys[pygame.K_a]:
    farmerX -= 1
  #d- right
  if keys[pygame.K_d]:
    farmerX +=1
  #w- up
  if keys[pygame.K_w]:
    farmerY -=1
  #s - down
  if keys[pygame.K_s]:
    farmerY +=1
  newFarmerRect = pygame.Rect(newFarmerX, newFarmerY, 50,50)

  
  #background
  screen.blit(grass, (0,0))
  #see if sheep have been sacked
  farmerRect = pygame.Rect(farmerX, farmerY, 50,50)
  for s in sheeps:
    screen.blit(sheepImage,(s[0],s[1]))
    if s.colliderect(farmerRect):
      sheeps.remove(s)
      score +=1
  #farmer
  screen.blit(farmerImage, (farmerX,farmerY))
  pygame.display.update()
  