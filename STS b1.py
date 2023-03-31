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

font = pygame.font.Font('freesansbold.ttf', 18)

#grass
grass= pygame.image.load('SackTheSheep/assets/grass-588.jpg')
grass = pygame.transform.scale(grass, (width, height))


#modifiable data for each level

#map
obstacles = [
   [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]
]
def reset():
    sheeps = [
       pygame.Rect(100,100,sheepSzX,sheepSzY),
       pygame.Rect(300,400,sheepSzX,sheepSzY),
       pygame.Rect(50,300,sheepSzX,sheepSzY)
    ]
    coins = [
       pygame.Rect(450,350,coinSize,coinSize),
       pygame.Rect(350,50,coinSize,coinSize)
    ]
    return sheeps, coins

#sheep 
sheepSzX = 55
sheepSzY = 45
sheepImage = pygame.image.load('SackTheSheep/assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (sheepSzX, sheepSzY))
#coins
coinSize = 20
coinImage = pygame.image.load('SackTheSheep/assets/coin.png')
coinImage = pygame.transform.scale(coinImage, (coinSize, coinSize))

sheeps, coins = reset()

#farmer
userSizeX = 38
userSizeY = 49
userSpeed = 0.3
spawnX = 50
spawnY = 50
farmerImage = pygame.image.load('SackTheSheep/assets/char.png')
farmerImage = pygame.transform.scale(farmerImage, (userSizeX, userSizeY))
farmerLeft = farmerImage.copy()
farmerLeft = pygame.transform.flip(farmerLeft, True, False)
user = entity.Player([spawnX,spawnY],userSpeed,[width,height],userSizeX,userSizeY,obstacles)

#home
homeImg = pygame.image.load("SackTheSheep/assets/farm.png")
homeImg = pygame.transform.scale(homeImg, (40,40))
homeRect = pygame.Rect(10,10,40,40)

home = False
score = 0
money = 0 #read from file
sackMax = 1 #read from file
sacked = 0
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
            sacked = 0
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

  if not sheeps and home:
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
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSizeX, userSizeY)
  for s in sheeps:
    screen.blit(sheepImage,(s[0],s[1]))
    #see if sheep have been sacked
    if s.colliderect(farmerRect) and sacked < sackMax:
      sheeps.remove(s)
      sacked += 1
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
  screen.blit(homeImg,(10,10))
  if homeRect.colliderect(farmerRect):
    sacked = 0
    home = True
  else:
    home = False
  #farmer
  if faceRight:
    screen.blit(farmerImage, (user.getPos()[0],user.getPos()[1]))
  else:
    screen.blit(farmerLeft, (user.getPos()[0],user.getPos()[1]))
  #text
  sackTxt = font.render("Sheep in Sack: " + str(sacked) + " / " + str(sackMax), True, (0,0,0))
  sacTxtRect = sackTxt.get_rect()
  sacTxtRect.center = (100, 480)
  screen.blit(sackTxt, sacTxtRect)
  leftTxt = font.render("Sheep left: " + str(len(sheeps)), True, (255,255,255))
  leftTxtRect = leftTxt.get_rect()
  leftTxtRect.center = (430, 20)
  screen.blit(leftTxt, leftTxtRect)

  #update display
  pygame.display.update()