import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *
import random
import entity

#initial game/screen setup
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Sack The Sheep')

font = pygame.font.Font('freesansbold.ttf', 18)
def genText(txt, colour, pos, posType):
  '''
  Blit's text to screen
  Parameters
  -----
  txt : Str
    Text that will be displayed
  colour : int ( )
    RGB colour of text
  pos : int [ ]
    x and y position of text
  posType : Str
    "top-right", "bottom-left", "bottom-right", or "top-left"
  '''
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
  screen.blit(rendered,rendRect)
  
#grass
grass = pygame.image.load('SackTheSheep/assets/grass-588.jpg')
grass = pygame.transform.scale(grass, (width, height))


#modifiable data for each level

#map
obstacles = [
   [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]
]
obstImages = []
imageLinks = ["SackTheSheep/assets/obstacles/0.png","SackTheSheep/assets/obstacles/1.png","SackTheSheep/assets/obstacles/3.png","SackTheSheep/assets/obstacles/4.png"]
for i in imageLinks:
  obstImage = pygame.image.load(i)
  obstImage = pygame.transform.scale(obstImage, (50,50))
  obstImages.append(obstImage)
for i in obstacles:
  i.append(random.randint(0,3))

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
sheepSzX = 30
sheepSzY = 24
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
defaultSpeed = 0.2
sprintSpeed = 0.8
spawnX = 50
spawnY = 50
farmerImage = pygame.image.load('SackTheSheep/assets/char.png')
farmerImage = pygame.transform.scale(farmerImage, (userSizeX, userSizeY))
farmerLeft = farmerImage.copy()
farmerLeft = pygame.transform.flip(farmerLeft, True, False)
user = entity.Player([spawnX,spawnY],defaultSpeed,[width,height],userSizeX,userSizeY,obstacles)

#home
homeImg = pygame.image.load("SackTheSheep/assets/house.png")
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
  if pressed[K_LEFT] or pressed[K_a]:
    faceRight = False
    user.moveLeft()
  if pressed[K_DOWN] or pressed[K_s]:
    user.moveDown()
  if pressed[K_UP] or pressed[K_w]:
    user.moveUp()
  if pressed[K_LCTRL]:
    user.setSpeed(sprintSpeed)
  else:
    user.setSpeed(defaultSpeed)

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
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSizeX, userSizeY)
  #sheep
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
    toBlit = obstImages[i[4]]
    screen.blit(toBlit,(i[0],i[1]))
    # obst = pygame.Rect(i[0],i[1],i[2],i[3])
    # pygame.draw.rect(screen,(80,40,10),obst)
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
  genText("Current Sheep in Sack: " + str(sacked) + "/" + str(sackMax), (50,50,50), [490,10], "bottom-left")
  genText("Sheep Left: " + str(len(sheeps)), (250,250,250), [10,490], "top-right")
  genText("Coins: " + str(money),(250,250,0),[40,490], "top-right")

  #update display
  pygame.display.update()