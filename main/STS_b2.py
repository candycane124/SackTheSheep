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
        [50,300,True],
        [20,470,False]
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
  sprintGen = info[5]

#map
match level:
  case 1:
    obstacles = [
      [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50],[0,400,50,50]
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
imageLinks = ["assets/obstacles/x0.png","assets/obstacles/x1.png","assets/obstacles/x2.png","assets/obstacles/3.png","assets/obstacles/4.png","assets/obstacles/5.png"]
for i in imageLinks:
  obstImage = pygame.image.load(i)
  obstImage = pygame.transform.scale(obstImage, (50,50))
  obstImages.append(obstImage)
for i in obstacles:
  i.append(random.randint(0,len(imageLinks)-1))

#health
healthImg = pygame.image.load("assets/heart.png")
healthImg = pygame.transform.scale(healthImg, (20,17))

#sheep 
sheepSzX = 30
sheepSzY = 24
sheepImage = pygame.image.load('assets/sheep.png')
sheepImage = pygame.transform.scale(sheepImage, (sheepSzX, sheepSzY))
sheepFlipped = sheepImage.copy()
sheepFlipped = pygame.transform.flip(sheepFlipped, True, False)
guiSheep = pygame.transform.scale(sheepImage, (14,11))

#wolf 
wolfW = 35
wolfH = 27
wolfVW = 22
wolfVH = 35
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
wolfMaskHorz = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfRunRight\wolfFrame6.png"),(wolfW,wolfH)))
wolfMaskVert = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfForward\wolfFront4.png"),(wolfW,wolfH))) 


#coins
coinSize = 20
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
guiCoin = pygame.image.load('assets/coinAnimate/sprite_0.png')
guiCoin = pygame.transform.scale(guiCoin, (14, 14))

sheeps, coins = reset(level)

guiSack = pygame.image.load('assets\sack.png')
guiSack = pygame.transform.scale(guiSack, (14,14))

#farmer
userSizeX = 38
userSizeY = 38
defaultSpeed = 1
sprintSpeed = 1
spawnX = 50
spawnY = 50
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
user = entity.Player([spawnX,spawnY],defaultSpeed,[width,height],userSizeX,userSizeY,3,obstImages,obstacles)
userMask = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets/farmerRun/Hobbit - run7.png"),(38,38)))

#home
homeImg = pygame.image.load("assets/house.png")
homeImg = pygame.transform.scale(homeImg, (40,40))
homeRect = pygame.Rect(10,10,40,40)

#alien rays
if level == 3:
  rayImg = pygame.image.load("assets/flame.png")
  rayImg = pygame.transform.scale(rayImg, (50,50))
  buildImg = pygame.image.load("assets/caution1.png")
  buildImg = pygame.transform.scale(buildImg, (50,50))
  alienEvent = pygame.USEREVENT+1
  pygame.time.set_timer(alienEvent, 3000)

#win/lose
winImg = pygame.image.load('assets/win.jpg')
winImg = pygame.transform.scale(winImg, (width, height))
loseImg = pygame.image.load('assets/gameover.jpg')
loseImg = pygame.transform.scale(loseImg, (width, height))







#main
win = False
home = False
score = 0
sacked = 0
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
sprint = 1000
timer = 0
while running:
  clock.tick(100)
  timer += 1
  # ------
  # EVENTS
  # ------
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
            user.changeHealth([3])
            sheeps, coins = reset(level)
            if level == 3:
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
      if level == 3 and event.type == alienEvent:
        buildUp = abduct(numRay,50,[width,height])
  # ----------
  # ALIEN RAYS
  # ----------
  if buildUp or rays:
    timeSince += clock.get_rawtime()
  if buildUp and timeSince >= 1000:
    rays = buildUp
    buildUp = []
    timeSince = 0
  if rays and timeSince >= 1600:
    nRI += 1
    if nRI == numRay*2:
      nRI = 0
      numRay += 1
    rays = []
    timeSince = 0
    
  # ------------------
  # CHARACTER MOVEMENT
  # ------------------
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
  if pressed[K_LSHIFT] and sprint > 10:
    user.setSpeed(sprintSpeed)
    sprint -= 5
    stop = False
  else:
    user.setSpeed(walkSpeed)
  if pressed[K_h]:
    user.setSpeed(2)
    sackMax = 3
  if not pressed[K_RIGHT] and not pressed[K_d] and not pressed[K_LEFT] and not pressed[K_a] and not pressed[K_DOWN] and not pressed[K_s] and not pressed[K_UP] and not pressed[K_w]:
    stop = True
  if sprint < 1000:
    sprint += sprintGen

  #win conditions
  if not sheeps and home:
    win = True
    running = False

  # ------
  # OUTPUT
  # ------
  # BACKGROUND
  screen.blit(grass, (0,0))
  farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSizeX, userSizeY)
  # SHEEP
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
      score += 50
  # COINS
  for c in coins:
    coinAnimation.draw(screen,c[0],c[1])
    coinAnimation.update()
    if c.colliderect(farmerRect):
       coins.remove(c)
       money += 1
       score += 10
  # WOLVES
  if level != 1:
    #horizontal wolves
    for w in wolfHorz:
      if w[0] >= 450:
        horzDirection = "left"
      if w[0] <= 150:
        horzDirection = "right"
      if horzDirection == "right":
        wolfAnimation.draw(screen, w[0], w[1])
        w[0]+= 1
        wolfAnimation.update()
      else:
        wolfLeftAnimation.draw(screen, w[0], w[1])
        w[0]-= 1
        wolfLeftAnimation.update()
      if wolfMaskHorz.overlap(userMask, (w[0]-user.getPos()[0],w[1]-user.getPos()[1])) and lifeStatus:
        user.changeHealth()
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
        # pygame.time.delay(8)
        wolfFrontAnimation.update()
      else:
        wolfBackAnimation.draw(screen, w[0], w[1])
        w[1]-= 1
        wolfBackAnimation.update()
      if wolfMaskVert.overlap(userMask, (w[0]-user.getPos()[0],w[1]-user.getPos()[1])) and lifeStatus:
        user.changeHealth()
        lifeStatus = False
  # OBSTACLES
  for i in obstacles:
    toBlit = obstImages[i[4]]
    screen.blit(toBlit,(i[0],i[1]))
  # HOUSE
  screen.blit(homeImg,(10,10))
  if homeRect.colliderect(farmerRect):
    sacked = 0
    home = True
  else:
    home = False
  # RAYS
  for i in buildUp:
    screen.blit(buildImg, (i[0],i[1]))
  for i in rays:
    screen.blit(rayImg, (i[0],i[1]))
    if i.colliderect(farmerRect) and lifeStatus:
      user.changeHealth()
      lifeStatus = False
  # CHARACTER
  if faceRight==True  and stop == False and lifeStatus == True:
    farmerRightAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerRightAnimation.update()
  if faceRight == False and stop == False and lifeStatus == True:
    farmerLeftAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerLeftAnimation.update()
  if faceRight == True and stop == True and lifeStatus == True:
    farmerStopRightAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerStopRightAnimation.update()
  if faceRight == False and stop == True and lifeStatus == True:
    farmerStopLeftAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerStopLeftAnimation.update()
  # DEATH
  if lifeStatus == False:
    farmerDeadAnimation.draw(screen, user.getPos()[0],user.getPos()[1])
    farmerDeadAnimation.update()
    if farmerDeadAnimation.getIndex() == 11:
      lifeStatus = True
      user.setPos([spawnX,spawnY])
      sacked = 0
      sheep, x = reset(level)
      farmerDeadAnimation.resetIndex()
      if level == 3:
        nRI = 0
        timeSince = 0
        pygame.time.set_timer(alienEvent, 0)
        pygame.time.set_timer(alienEvent, 3000)
        rays = []
        buildUp = []
      if user.getHealth() == 0:
        if score >= 150:
          score -= 150
        running = False
  # SPRINT
  pygame.draw.rect(screen,(40,40,40),(200,5,100,10))
  pygame.draw.rect(screen,(20,100,250),(200,5,sprint/10,10))
  # HEALTH
  for i in range(user.getHealth()):
    screen.blit(healthImg, (220+i*22,20))

  # ----
  # TEXT
  # ----
  #sheep
  screen.blit(guiSheep,(482,7))
  genText(str(len(sheeps)), (40,40,40), [6,478], "top-right")
  #coin
  screen.blit(guiCoin, (482,30))
  genText(str(money),(255,195,0), [31,478], "top-right")
  #sack
  screen.blit(guiSack, (482, 55))
  genText(str(sacked) + "/" + str(sackMax), (0,0,0), [55,478], "top-right")

  # UPDATE DISPLAY
  pygame.display.update()

starImg = pygame.transform.scale(pygame.image.load("assets\star.png"),(20,20))
score += user.getHealth()*100
timePenalty = timer//100
if score >= timePenalty:
  score -= timePenalty
elif win:
  score = 10
else:
  score = 0
if win:
  with open('main/stats.txt','r') as textFile:
    file_content = textFile.readlines()
    infoLine = list(map(float,file_content[0].split()))
    infoLine[3] += money
    if level != 3:
      infoLine[0] += 1
  with open('main/stats.txt','w') as outFile:
    outText = ""
    for i in infoLine:
      outText += str(i) + " "
    outText += "\nlevel walkSpeed sprintSpeed money sackMax sprintGen"
    outFile.write(outText) 

#level cleared
while win:
  for event in pygame.event.get():
    if event.type == QUIT:
      #quit game
      pygame.quit()
      sys.exit()
  screen.blit(winImg, (0,0))
  genText("Score: " + str(score), (0,0,0), [250,400], "middle")
  if score >= 470: # need to test values
    stars = 3
  elif score >= 410:
    stars = 2
  elif score >= 300:
    stars = 1
  else:
    stars = 0
  for i in range(stars):
    screen.blit(starImg, (200+i*50,420))
  pygame.display.update()
  #send user to success page/choose levels page

while not win:
  for event in pygame.event.get():
    if event.type == QUIT:
      #quit game
      pygame.quit()
      sys.exit()
  screen.blit(loseImg, (0,0))
  genText("Score: " + str(score), (250,250,250), [250,400], "middle")
  pygame.display.update()