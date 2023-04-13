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

#easier text generation
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
    y, x position of text
  posType : Str
    "top-right", "bottom-left", "bottom-right", "top-left", or "middle"
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
  elif posType == "middle":
    rendRect.center = (pos[0], pos[1])
  screen.blit(rendered,rendRect)


#reset level function
def reset(level):
  match level:
    case 1:
      sheeps = [
        [100,100,False],
        [300,400,True],
        [50,300,False]
      ]
      coins = [
        pygame.Rect(450,350,coinSize,coinSize),
        pygame.Rect(350,50,coinSize,coinSize)
      ]
    case 2:
      sheeps = [
        [210,220,True],
        [60,320,False],
        [410,120,False],
        [360,440,True]
      ]
      coins = [
        pygame.Rect(450,390,coinSize,coinSize),
        pygame.Rect(300,50,coinSize,coinSize),
        pygame.Rect(140,440,coinSize,coinSize),
        pygame.Rect(20,250,coinSize,coinSize),
        pygame.Rect(300,300,coinSize,coinSize)
      ]
    case 3:
      sheeps = [
        [210,220,True],
        # [60,320,False],
        # [410,120,False],
        # [360,440,True]
      ]
      coins = [
        pygame.Rect(450,390,coinSize,coinSize),
        pygame.Rect(300,50,coinSize,coinSize),
        pygame.Rect(140,440,coinSize,coinSize),
        pygame.Rect(20,250,coinSize,coinSize),
        pygame.Rect(300,300,coinSize,coinSize)
      ]
  return sheeps, coins
  
def abduct(n,raySize,maxMap):
    areas = []
    secX = maxMap[0]//raySize
    secY = maxMap[1]//raySize
    for i in range(n):
        nX = random.randint(0,secX-1)
        nY = random.randint(0,secY-1)
        areas.append(pygame.Rect(nX*raySize,nY*raySize,raySize,raySize))
    return areas

#grass
grass = pygame.image.load('assets/grass-588.jpg')
grass = pygame.transform.scale(grass, (width, height))

#modifiable user data from text file
with open('main\stats.txt','r') as textFile:
  file_content = textFile.readlines()
  info = list(map(float,file_content[0].split()))
  level = info[0]
  walkSpeed = info[1]
  sprintSpeed = info[2]
  money = int(info[3])
  sackMax = int(info[4])

#map
match level:
  case 1:
    obstacles = [
      [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]
    ]
  case 2:
    obstacles = [
      [0,300,50,50],[0,450,50,50],[50,250,50,50],[150,0,50,50],[200,400,50,50],[250,150,50,50],[350,300,50,50],[350,100,50,50],[450,50,50,50]
    ]
  case 3:
    obstacles = [
      [0,300,50,50],[0,450,50,50],[50,250,50,50],[150,0,50,50],[200,400,50,50],[250,150,50,50],[350,300,50,50],[350,100,50,50],[450,50,50,50]
    ]
obstImages = []
imageLinks = ["assets/obstacles/0.png","assets/obstacles/1.png","assets/obstacles/3.png","assets/obstacles/4.png","assets/obstacles/5.png"]
for i in imageLinks:
  obstImage = pygame.image.load(i)
  obstImage = pygame.transform.scale(obstImage, (50,50))
  obstImages.append(obstImage)
for i in obstacles:
  i.append(random.randint(0,3))

#farmer
userSizeX = 38
userSizeY = 49
spawnX = 50
spawnY = 50
farmerImage = pygame.image.load('assets/char.png')
farmerImage = pygame.transform.scale(farmerImage, (userSizeX, userSizeY))
farmerLeft = farmerImage.copy()
farmerLeft = pygame.transform.flip(farmerLeft, True, False)
user = entity.Player([spawnX,spawnY],walkSpeed,[width,height],userSizeX,userSizeY,obstacles)

#sheep 
sheepSzX = 30
sheepSzY = 24
sheepImage = pygame.image.load('assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (sheepSzX, sheepSzY))
sheepFlipped = sheepImage.copy()
sheepFlipped = pygame.transform.flip(sheepFlipped, True, False)
#coins
coinSize = 20
coinImage = pygame.image.load('assets/coin.png')
coinImage = pygame.transform.scale(coinImage, (coinSize, coinSize))

sheeps, coins = reset(level)

#home
homeImg = pygame.image.load("assets/house.png")
homeImg = pygame.transform.scale(homeImg, (40,40))
homeRect = pygame.Rect(10,10,40,40)

#alien rays
if level == 3:
  rayImg = pygame.image.load("assets/red.png")
  rayImg = pygame.transform.scale(rayImg, (50,50))
  alienEvent = pygame.USEREVENT+1
  pygame.time.set_timer(alienEvent, 4000)

#
winImg = pygame.image.load('assets/win.jpg')
winImg = pygame.transform.scale(winImg, (width, height))

#main
win = False
home = False
score = 0
sacked = 0
health = 800
faceRight = True
running = True
rays = []
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
            health = 800
            sheeps, coins = reset(level)
          elif event.key == K_ESCAPE:
            #send to pause or menu screen
            pass
      if event.type == alienEvent:
        rays = abduct(4,50,[width,height])
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
    user.setSpeed(walkSpeed)

  if not sheeps and home:
    win = True
    running = False
  if health <= 0:
    user.setPos([spawnX,spawnY])
    score = 0
    money = 0
    sacked = 0
    health = 800
    sheeps, coins = reset(level)

  #------------
  #OUTPUT
  #------------ 
  #background
  screen.blit(grass, (0,0))
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSizeX, userSizeY)

  #sheep
  for s in sheeps:
    current = pygame.Rect(s[0],s[1],sheepSzX,sheepSzY)
    if s[2]:
      screen.blit(sheepFlipped,(current[0],current[1]))
    else:
      screen.blit(sheepImage,(current[0],current[1]))
    #see if sheep have been sacked
    if current.colliderect(farmerRect) and sacked < sackMax:
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
  screen.blit(homeImg,(10,10))
  if homeRect.colliderect(farmerRect):
    sacked = 0
    home = True
  else:
    home = False
  #rays
  for i in rays:
    screen.blit(rayImg, (i[0],i[1]))
    if i.colliderect(farmerRect):
      health -= 1
  #farmer
  if faceRight:
    screen.blit(farmerImage, (user.getPos()[0],user.getPos()[1]))
  else:
    screen.blit(farmerLeft, (user.getPos()[0],user.getPos()[1]))
  #text
  genText("Current Sheep in Sack: " + str(sacked) + "/" + str(sackMax), (50,50,50), [490,10], "bottom-left")
  genText("Sheep Left: " + str(len(sheeps)), (250,250,250), [10,490], "top-right")
  genText("Coins: " + str(money),(250,250,0),[40,490], "top-right")
  genText("Health: " + str(health//80), (200,20,60), [70,490], "top-right")

  #update display
  pygame.display.update()

#level cleared
while win:
  for event in pygame.event.get():
    if event.type == QUIT:
      #quit game
      pygame.quit()
      sys.exit()
  screen.blit(winImg, (0,0))
  pygame.display.update()
  #send user to success page/choose levels page
