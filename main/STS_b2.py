import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *
import random
import entity
import animate

#initial game/screen setup
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Sack The Sheep')

#easier text generation
font = pygame.font.Font('freesansbold.ttf', 14)
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

#health
healthImg = pygame.image.load("assets/heart.png")
healthImg = pygame.transform.scale(healthImg, (13,11))

#sheep 
sheepSzX = 30
sheepSzY = 24
sheepImage = pygame.image.load('assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (sheepSzX, sheepSzY))
sheepFlipped = sheepImage.copy()
sheepFlipped = pygame.transform.flip(sheepFlipped, True, False)

#wolf 
wolfW = 35
wolfH=27
wolfVW = 22
wolfVH=35
wolfX = 150
wolfY = 90

#wolf animation running right
wolfAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame1.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame2.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame3.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame4.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame5.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame6.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunRight/wolfFrame7.png'), (wolfW,wolfH))
  
])
wolfLeftAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft1.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft2.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft3.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft4.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft5.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft6.png'), (wolfW,wolfH)),
  pygame.transform.scale(pygame.image.load('assets/wolfRunLeft/wolfLeft7.png'), (wolfW,wolfH))
])
wolfFrontAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront1.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront2.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront3.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront4.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront5.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront6.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfForward/wolfFront7.png'), (wolfVW,wolfVH))
])
wolfBackAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack1.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack2.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack3.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack4.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack5.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack6.png'), (wolfVW,wolfVH)),
  pygame.transform.scale(pygame.image.load('assets/wolfBack/wolfBack7.png'), (wolfVW,wolfVH))
  
])
wolfHorz = [
  pygame.Rect(wolfX,wolfY,wolfW,wolfH)
]
wolfVert = [
  pygame.Rect(wolfX+100,wolfY+70,wolfVW,wolfVH)
]

#coins
coinSize = 20
#coinImage = pygame.image.load('assets/coin.png')
coinAnimation = animate.Animate([
  pygame.image.load('assets/coinAnimate/sprite_0.png'),
  pygame.image.load('assets/coinAnimate/sprite_1.png'),
  pygame.image.load('assets/coinAnimate/sprite_2.png'),
  pygame.image.load('assets/coinAnimate/sprite_3.png'),
  pygame.image.load('assets/coinAnimate/sprite_4.png'),
  pygame.image.load('assets/coinAnimate/sprite_5.png'),
  pygame.image.load('assets/coinAnimate/sprite_6.png'),
  pygame.image.load('assets/coinAnimate/sprite_7.png'),
  pygame.image.load('assets/coinAnimate/sprite_8.png')
])
#coinImage = pygame.transform.scale(coinImage, (coinSize, coinSize))

sheeps, coins = reset(level)

#farmer
userSizeX = 38
userSizeY = 38
defaultSpeed = 1
sprintSpeed = 1
spawnX = 50
spawnY = 50
#farmerImage = pygame.image.load('assets/char.png')
farmerRightAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run1.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run3.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run4.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run5.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run6.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run7.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run8.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run9.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run10.png'),(userSizeX, userSizeY))
])
farmerLeftAnimation = animate.Animate([
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run1.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run2.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run3.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run4.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run5.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run6.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run7.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run8.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run9.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run10.png'),(userSizeX, userSizeY)),True, False)
])
farmerStopRightAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle1.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle1.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY))
])
farmerStopLeftAnimation = animate.Animate([
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle1.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle1.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle2.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle3.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY)),True, False),
  pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/farmerStop/Hobbit - Idle4.png'),(userSizeX, userSizeY)),True, False)
])
farmerDeadAnimation = animate.Animate([
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death1.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death2.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death3.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death4.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death5.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death6.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death7.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death8.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death9.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death10.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death11.png'),(userSizeX, userSizeY)),
  pygame.transform.scale(pygame.image.load('assets/farmerDie/Hobbit - death12.png'),(userSizeX, userSizeY)),
])
user = entity.Player([spawnX,spawnY],defaultSpeed,[width,height],userSizeX,userSizeY,obstacles)

#home
homeImg = pygame.image.load("assets/house.png")
homeImg = pygame.transform.scale(homeImg, (40,40))
homeRect = pygame.Rect(10,10,40,40)

#alien rays
if level == 3:
  rayImg = pygame.image.load("assets/flame.png")
  rayImg = pygame.transform.scale(rayImg, (50,50))
  buildImg = pygame.image.load("assets/caution.png")
  buildImg = pygame.transform.scale(buildImg, (50,50))
  alienEvent = pygame.USEREVENT+1
  pygame.time.set_timer(alienEvent, 3000)

#win
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
stop = False
lifeStatus = True
horzDirection = "right"
vertDirection = "down"
timeSince = 0
numRay = 1
nRI = 0
rays = []
buildUp = []
while running:
  clock.tick()
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
            numRay = 1
            nRI = 0
            timeSince = 0
            pygame.time.set_timer(alienEvent, 0)
            pygame.time.set_timer(alienEvent, 3000)
            rays = []
            buildUp = []
          elif event.key == K_ESCAPE:
            #send to pause or menu screen
            pass
      if event.type == alienEvent:
        buildUp = abduct(numRay,50,[width,height])
  if buildUp or rays:
    timeSince += clock.get_rawtime()
  if buildUp and timeSince >= 800:
    rays = buildUp
    buildUp = []
    timeSince = 0
  if rays and timeSince >= 1500:
    nRI += 1
    if nRI == 3:
      nRI = 0
      numRay += 1
    rays = []
    timeSince = 0
    
  #keyboard input for character movement
  pressed = pygame.key.get_pressed()
  if pressed[K_RIGHT] or pressed[K_d]:
    faceRight = True
    stop= False
    user.moveRight()
  if pressed[K_LEFT] or pressed[K_a]:
    faceRight = False
    stop = False
    user.moveLeft()
  if pressed[K_DOWN] or pressed[K_s]:
    stop = False
    user.moveDown()
  if pressed[K_UP] or pressed[K_w]:
    stop= False
    user.moveUp()
  if pressed[K_LCTRL]:
    user.setSpeed(sprintSpeed)
    stop = False
  else:
    user.setSpeed(walkSpeed)
  if not pressed[K_RIGHT] and not pressed[K_d] and not pressed[K_LEFT] and not pressed[K_a] and not pressed[K_DOWN] and not pressed[K_s] and not pressed[K_UP] and not pressed[K_w]:
    stop = True

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
    numRay = 1
    nRI = 0
    timeSince = 0
    pygame.time.set_timer(alienEvent, 0)
    pygame.time.set_timer(alienEvent, 3000)
    rays = []
    buildUp = []

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
  for c in coins:
    coinAnimation.draw(screen,c[0],c[1])
    coinAnimation.update()
    if c.colliderect(farmerRect):
       coins.remove(c)
       money += 1
  #horizontal wolves
  for w in wolfHorz:
    if w[0] >= 450:
      horzDirection = "left"
    if w[0] <= 150:
      horzDirection = "right"
    if horzDirection == "right":
      wolfAnimation.draw(screen, w[0], w[1])
      w[0]+= 1
      #pygame.time.delay(5)
      wolfAnimation.update()
    else:
      wolfLeftAnimation.draw(screen, w[0], w[1])
      w[0]-= 1
      wolfLeftAnimation.update()
    if w.colliderect(farmerRect) and lifeStatus:
      health -= 80
      lifeStatus = False

  #vertical wolves
  for w in wolfVert:
    if w[1] >= 450:
      vertDirection = "up"
    if w[1] <= 180:
      vertDirection = "down"
    if vertDirection == "down":
      wolfFrontAnimation.draw(screen, w[0], w[1])
      w[1]+= 1
      pygame.time.delay(8)
      wolfFrontAnimation.update()
    else:
      wolfBackAnimation.draw(screen, w[0], w[1])
      w[1]-= 1
      pygame.time.delay(8)
      wolfBackAnimation.update()
    if w.colliderect(farmerRect) and lifeStatus:
      health -= 80
      lifeStatus = False
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
  for i in buildUp:
    screen.blit(buildImg, (i[0],i[1]))
  for i in rays:
    screen.blit(rayImg, (i[0],i[1]))
    if i.colliderect(farmerRect):
      health -= 1
  #farmer
  if faceRight==True  and stop == False and lifeStatus == True:
    farmerRightAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerRightAnimation.update()
    #screen.blit(farmerImage, (user.getPos()[0],user.getPos()[1]))
  if faceRight == False and stop == False and lifeStatus == True:
    farmerLeftAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerLeftAnimation.update()
    #screen.blit(farmerLeft, (user.getPos()[0],user.getPos()[1]))
  if faceRight == True and stop == True and lifeStatus == True:
    farmerStopRightAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerStopRightAnimation.update()
  if faceRight == False and stop == True and lifeStatus == True:
    farmerStopLeftAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerStopLeftAnimation.update()
  if lifeStatus == False:
    farmerDeadAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerDeadAnimation.update()
    if farmerDeadAnimation.getIndex() == 11:
      lifeStatus = True
      user.setPos([spawnX,spawnY])
      score = 0
      money = 0
      sacked = 0
      sheeps, coins = reset()
      farmerDeadAnimation.resetIndex()
  #text
  # genText("Current Sheep in Sack: " + str(sacked) + "/" + str(sackMax), (50,50,50), [490,10], "bottom-left")
  genText("Sheep Left: " + str(len(sheeps)), (250,250,250), [5,496], "top-right")
  genText("Coins: " + str(money),(250,250,0), [30,496], "top-right")
  genText("Sacked: " + str(sacked) + "/" + str(sackMax), (50,50,50), [55,496], "top-right")
  # genText("Health: " + str(health//80), (200,20,60), [70,490], "top-right")
  for i in range(health//80+1):
    screen.blit(healthImg, (500-i*15,485))

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
