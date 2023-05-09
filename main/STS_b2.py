import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *
import random
import entity
import animate
import sound

#easier text generation
def genText(screen, txt, colour, pos, posType):
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
  font = pygame.font.Font('freesansbold.ttf', 14)
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

#reset level function
def reset(level):
  coinSize = 20
  match level:
    case 1:
      sheeps = [
        [100,100,False],
        [300,400,True],
        [50,300,True],
        # [20,470,False]
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
        [170,70,True],
        [400,160,False],
        [10,360,False],
        [240,450,True],
        [430,410,True]
      ]
      coins = [
        pygame.Rect(460,70,coinSize,coinSize),
        pygame.Rect(100,180,coinSize,coinSize),
        pygame.Rect(420,240,coinSize,coinSize),
        pygame.Rect(270,290,coinSize,coinSize),
        pygame.Rect(20,470,coinSize,coinSize)
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

def startLevel(level):
  #initial game/screen setup
  pygame.init()
  width = 500
  height = 500
  screen = pygame.display.set_mode((width, height))
  clock = pygame.time.Clock()
  pygame.display.set_caption('Sack The Sheep')

  #grass
  grass = pygame.image.load('assets/grass-588.jpg')
  grass = pygame.transform.scale(grass, (width, height))

  #modifiable user data from text file
  with open('main\stats.txt','r') as textFile:
    file_content = textFile.readlines()
    info = list(map(float,file_content[0].split()))
    # level = info[0]
    walkSpeed = info[1]
    sprintSpeed = walkSpeed*1.15
    money = int(info[2])
    sackMax = int(info[3])
    sprintGen = info[4]

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
        [100,50,50,50],[400,0,50,50],[200,100,50,50],[50,200,50,50],[350,200,50,50],[150,250,50,50],[150,300,50,50],[200,300,50,50],[450,250,50,50],[400,350,50,50],[150,400,50,50],[450,400,50,50],[50,450,50,50]
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

  #WOLVES
  # wolf 
  wolfW = 35
  wolfH = 27
  wolfVW = 22
  wolfVH = 35
  wolfX = 150
  wolfY = 90

  #Horizontal Wolves
  wolfR = animate.Animate('wolfR')

  #Vertical Wolves
  wolfF = animate.Animate('wolfF')
  wolfB = animate.Animate('wolfB')
  if level == 2:
    wolfHorz = [
      [pygame.Rect(wolfX,wolfY,wolfW,wolfH),[wolfX,465]]
    ]
    wolfVert = [
      pygame.Rect(wolfX+100,wolfY+70,wolfVW,wolfVH)
    ]
  elif level == 3:
    wolfHorz = [
      [pygame.Rect(200,270,wolfW,wolfH),[200,415]],
      [pygame.Rect(100,370,wolfW,wolfH),[20,350]]
    ]
    wolfVert = []

  wolfMaskHorz = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfRunRight\wolfFrame6.png"),(wolfW,wolfH)))
  wolfMaskVert = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfForward\wolfFront4.png"),(wolfW,wolfH))) 


  #coins
  coinSize = 20
  coinAnimate = animate.Animate('coin')

  sheeps, coins = reset(level)
  guiCoin = pygame.image.load('assets\coin.png')
  guiSack = pygame.image.load('assets\sack.png')
  guiSack = pygame.transform.scale(guiSack, (14,14))

  #-------------------------
  #       FARMER
  #-------------------------
  userSizeX = 38
  userSizeY = 38
  defaultSpeed = 1
  sprintSpeed = 1
  spawnX = 50
  spawnY = 50
  user = entity.Player([spawnX,spawnY],defaultSpeed,[width,height],userSizeX,userSizeY,3,obstImages,obstacles)
  userMask = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets/farmerRun/Hobbit - run7.png"),(38,38)))
  farmDie = animate.Animate('farmDie')
  farmRun = animate.Animate('farmRun')
  farmStop = animate.Animate('farmStop')

  #home
  homeImg = pygame.image.load("assets/house.png")
  homeImg = pygame.transform.scale(homeImg, (40,40))
  homeRect = pygame.Rect(10,10,40,40)

  #alien rays
  if level == 3:
    buildImg = pygame.image.load("assets/caution1.png")
    buildImg = pygame.transform.scale(buildImg, (50,50))
    alienEvent = pygame.USEREVENT+1
    pygame.time.set_timer(alienEvent, 4900)
  #alien 
  smokeW = 50
  smokeH = 50
  smoke = animate.Animate('smoke')

  #win/lose
  winImg = pygame.image.load('assets/win.png')
  winImg = pygame.transform.scale(winImg, (width, height))

  loseImg = pygame.image.load('assets/gameover.jpg')
  loseImg = pygame.transform.scale(loseImg, (width, height))

  #---------------------------------
  #          SOUND/MUSIC
  #---------------------------------
  coinSound = sound.Sound('coin')
  packSheepSound = sound.Sound('sheep')
  alarmSound = sound.Sound('alarm')
  alienSmoke = sound.Sound('alienSmoke')
  hitSound = sound.Sound('hit')
  level1M = sound.Music('level1')
  level2M = sound.Music('level2')
  level3M = sound.Music('level3')
  menuMusic = sound.Music('menu')
  if level == 1:
    level1M.playMusic()
  if level == 2:
    level2M.playMusic()
  if level == 3:
    level3M.playMusic()
  # menuMusic.playMusic()


  #---------------------------------
  #              MAIN
  #---------------------------------
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
    timer += 1
    clock.tick(100)

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
              sprint = 1000
              timer = 0
              user.changeHealth([3])
              sheeps, coins = reset(level)
              if level == 3:
                numRay = 1
                nRI = 0
                timeSince = 0
                pygame.time.set_timer(alienEvent, 0)
                pygame.time.set_timer(alienEvent, 4900)
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
    if buildUp and timeSince >= 950:
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
      stop = False
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
        packSheepSound.play()
        sheeps.remove(s)
        sacked += 1
        score += 50
    # COINS
    for c in coins:
      coinAnimate.draw(screen,c[0],c[1], coinSize, coinSize,False, False)
      coinAnimate.update()
      if c.colliderect(farmerRect):
        coinSound.playSound()
        coins.remove(c)
        money += 1
        score += 10
    if level != 1:
      #horizontal wolves
      for w in wolfHorz:
        if w[0][0] >= w[1][1]:
          horzDirection = "left"
        if w[0][0] <= w[1][0]:
          horzDirection = "right"
        if horzDirection == "right":
          wolfR.draw(screen, w[0][0], w[0][1], wolfW, wolfH, False, False)
          w[0][0] += 1
          wolfR.update()
        #Wolf run left
        else:
          wolfR.draw(screen, w[0][0], w[0][1], wolfW, wolfH, True, False)
          w[0][0] -= 1
          wolfR.update()
        if wolfMaskHorz.overlap(userMask, (w[0][0]-user.getPos()[0],w[0][1]-user.getPos()[1])) and lifeStatus:
          user.changeHealth()
          lifeStatus = False

      #vertical wolves
      for w in wolfVert:
        if w[1] >= 450:
          vertDirection = "up"
        if w[1] <= 180:
          vertDirection = "down"
        if vertDirection == "down":
          wolfF.draw(screen, w[0], w[1], wolfVW, wolfVH, False,False)
          w[1]+= 1
          wolfF.update()
        else:
          wolfB.draw(screen, w[0], w[1], wolfVW, wolfVH, False, False)
          w[1]-= 1
          wolfB.update()
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
      alarmSound.playSound()
    for i in rays:
      smoke.draw(screen, i[0],i[1], smokeW, smokeH, False, False)
      smoke.update()
      if i.colliderect(farmerRect) and lifeStatus:
        alienSmoke.playSound()
        user.changeHealth()
        lifeStatus = False        
    # CHARACTER
    if faceRight==True  and stop == False and lifeStatus == True:
      farmRun.draw(screen, user.getPos()[0],user.getPos()[1],userSizeX, userSizeY, False, False)
      farmRun.update()
    #Farmer running left
    if faceRight == False and stop == False and lifeStatus == True:
      farmRun.draw(screen, user.getPos()[0],user.getPos()[1], userSizeX, userSizeY,True, False)
      farmRun.update()
    #Farmer stop right facing
    if faceRight == True and stop == True and lifeStatus == True:
      farmStop.draw(screen, user.getPos()[0],user.getPos()[1], userSizeX, userSizeY,False, False)
      farmStop.update()
    if faceRight == False and stop == True and lifeStatus == True:
      farmStop.draw(screen, user.getPos()[0],user.getPos()[1],userSizeX, userSizeY,True, False)
      farmStop.update()
    if lifeStatus == False:
      farmDie.draw(screen, user.getPos()[0],user.getPos()[1],userSizeX, userSizeY,False, False)
      farmDie.update()
      if farmDie.getIndex() == 11:
        lifeStatus = True
        user.setPos([spawnX,spawnY])
        sacked = 0
        if sprint < 500:
          sprint += 500
        else:
          sprint = 1000
        sheep, x = reset(level)
        farmDie.resetIndex()
        if level == 3:

          nRI = 0
          timeSince = 0
          pygame.time.set_timer(alienEvent, 0)
          pygame.time.set_timer(alienEvent, 4900)
          rays = []
          buildUp = []
        if user.getHealth() == 0:
          if score >= 150:
            score -= 150
          running = False
    # SPRINT
    pygame.draw.rect(screen,(40,40,40),(200,5,100,10))
    pygame.draw.rect(screen,(140,100,250),(200,5,sprint/10,10))
    # HEALTH
    for i in range(user.getHealth()):
      screen.blit(healthImg, (220+i*22,20))

    # ----
    # TEXT
    # ----
    #sheep
    screen.blit(guiSheep,(482,7))
    genText(screen,str(len(sheeps)), (40,40,40), [6,478], "top-right")
    #coin
    screen.blit(guiCoin, (482,30))
    genText(screen,str(money),(255,195,0), [31,478], "top-right")
    #sack
    screen.blit(guiSack, (482, 55))
    genText(screen,str(sacked) + "/" + str(sackMax), (0,0,0), [55,478], "top-right")

    # UPDATE DISPLAY
    pygame.display.update()

  starImg = pygame.transform.scale(pygame.image.load("assets\star.png"),(30,30))
  score += user.getHealth()*100
  timePenalty = timer//100
  print(timePenalty)
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
      infoLine[2] = money
      # if level != 3:
      #   infoLine[0] += 1
    with open('main/stats.txt','w') as outFile:
      outText = ""
      for i in infoLine:
        outText += str(i) + " "
      outText += "\nlevel walkSpeed money sackMax sprintGen"
      outFile.write(outText) 
    with open('main/scores.txt','a') as outFile:
      outText = f"{score} (level {level})\n"
      outFile.write(outText)

  #level cleared
  while win:
    for event in pygame.event.get():
      if event.type == QUIT:
        #quit game
        pygame.quit()
        sys.exit()
    screen.blit(winImg, (0,0))
    genText(screen,"Score: " + str(score), (0,0,0), [400,250], "middle")
    match level:
      case 1:
        if score >= 442: # need to test values
          stars = 3
        elif score >= 428:
          stars = 2
        elif score >= 410:
          stars = 1
        else:
          stars = 0
      case 2:
        if score >= 500:
          stars = 3
        elif score >= 390:
          stars = 2
        elif score >= 290:
          stars = 1
        else:
          stars = 0
      case 3:
        if score >= 500:
          stars = 3
        elif score >= 350:
          stars = 2
        elif score >= 250:
          stars = 1
        else:
          stars = 0
    
    for i in range(stars):
      screen.blit(starImg, (190+i*45,420))
    pygame.display.update()
    #send user to success page/choose levels page

  while not win:
    for event in pygame.event.get():
      if event.type == QUIT:
        #quit game
        pygame.quit()
        sys.exit()
    screen.blit(loseImg, (0,0))
    genText(screen,"Score: " + str(score), (250,250,250), [250,400], "middle")
    pygame.display.update()

startLevel(2)
