import pygame, sys
from pygame.locals import QUIT
from pygame.locals import *
import random
from game.entity import *
from game.animate import Animate
from game.sound import *

#easier text generation
def genText(screen, txt, colour, pos, posType, size=14):
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
  #set the font and size
  font = pygame.font.Font('freesansbold.ttf', size)
  #Render the text with specified font, text content and color
  rendered = font.render(txt, True, colour)
  #Get the rectangle that encloses the rendered text
  rendRect = rendered.get_rect()
  #Determine the posiiton of the rendered text based on specified position type
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
  #Draw the rendered text onto the screen at the specified position
  screen.blit(rendered,rendRect)

#reset level function
def reset(level):
  """
  Resets the game configuration based on the specified level.

  Args:
  -----
  level (int): The level of the game.

  Returns:
  -------
  tuple: A tuple containing two lists: `sheeps` and `coins`.
    - sheeps (list): A list of sheep configurations.
    - coins (list): A list of coin rectangles.

  """
  #Define the size of the coins
  coinSize = 20
  #Match the value of the 'level' parameter
  match level:
    #Configuration for level 1
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
    #Configuration for level 2
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
    #Configuration for level 3
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
  #Return the configured sheep and coin lists
  return sheeps, coins
  
def abduct(n,raySize,maxMap):
  """
  Generate a list of rectangular areas for exploding objects.

  Args:
  -----
  n (int): Number of areas to generate.
  raySize (int): Size of each area (width and height).
  maxMap (tuple): Maximum dimensions of the map (width, height).

  Returns:
  list: List of pygame.Rect objects representing the areas.

  """
  areas = []
  secX = maxMap[0]//raySize
  secY = maxMap[1]//raySize
  for i in range(n):
      nX = random.randint(0,secX-1)
      nY = random.randint(0,secY-1)
      areas.append(pygame.Rect(nX*raySize,nY*raySize,raySize,raySize))
  return areas

def startLevel(level, controller):
  """
  Start a new game level.

  Args:
  -----
  level (int): Level number.
  controller: Controller object for the game.

  """
  #Intialize pygame and set up the screen 
  pygame.init()
  width = 500
  height = 500
  screen = pygame.display.set_mode((width, height))
  clock = pygame.time.Clock()
  pygame.display.set_caption('Sack The Sheep')

  #Load and scale the grass image
  grass = pygame.image.load('assets/grass-588.jpg')
  grass = pygame.transform.scale(grass, (width, height))

  #Read modifiable user data from text file
  with open('game\stats.txt','r') as textFile:
    file_content = textFile.readlines()
    # Extract relevant information from the file
    info = list(map(float,file_content[0].split()))
    walkSpeed = info[1]
    sprintSpeed = walkSpeed+0.06
    money = int(info[2])
    sackMax = int(info[3])
    sprintGen = info[4]

  #Define the obstacles for each level/map
  match level:
    case 1:
      obstacles = [
        [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50],[0,400,50,50],[300,340,50,50]
      ]
    case 2:
      obstacles = [
        [0,300,50,50],[0,450,50,50],[50,250,50,50],[150,0,50,50],[200,400,50,50],[250,150,50,50],[350,300,50,50],[350,100,50,50],[450,50,50,50],[150,250,50,50]
      ]
    case 3:
      obstacles = [
        [100,50,50,50],[400,0,50,50],[200,100,50,50],[50,200,50,50],[350,200,50,50],[150,250,50,50],[150,300,50,50],[200,300,50,50],[450,250,50,50],[400,350,50,50],[150,400,50,50],[450,400,50,50],[50,450,50,50]
      ]
  #Load obstacle images
  obstImages = []
  imageLinks = ["assets/obstacles/x0.png","assets/obstacles/x1.png","assets/obstacles/x2.png","assets/obstacles/3.png","assets/obstacles/4.png","assets/obstacles/5.png"]
  for i in imageLinks:
    obstImage = pygame.image.load(i)
    obstImage = pygame.transform.scale(obstImage, (50,50))
    obstImages.append(obstImage)
  #Assign a random image to each obstacle 
  for i in obstacles:
    i.append(random.randint(0,len(imageLinks)-1))

  #Load health image
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

  #------------
  #  WOLVES
  #-----------
  # Intialize properties for the wolf character
  wolfW = 35
  wolfH = 27
  wolfVW = 22
  wolfVH = 35
  wolfX = 150
  wolfY = 90

  #Horizontal Wolves animation
  wolfR = Animate('wolfR')

  #Vertical Wolves animation
  wolfF = Animate('wolfF')
  wolfB = Animate('wolfB')
  #Define the position and masks for wolves based on current level
  if level == 2:
    #Defin horizontal wolves at specific postions
    wolfHorz = [
      [pygame.Rect(wolfX,wolfY,wolfW,wolfH),[wolfX,465]]
    ]
    #Defin vertical wolves (empty list)
    wolfVert = [
      pygame.Rect(wolfX+100,wolfY+70,wolfVW,wolfVH)
    ]
  elif level == 3:
    wolfHorz = [
      [pygame.Rect(200,270,wolfW,wolfH),[200,415]],
      [pygame.Rect(100,370,wolfW,wolfH),[20,350]]
    ]
    wolfVert = []

  #Create maks for the horizontal and vertical wolf images
  wolfMaskHorz = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfRunRight\wolfFrame6.png"),(wolfW,wolfH)))
  wolfMaskVert = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets\wolfForward\wolfFront4.png"),(wolfW,wolfH))) 


  #coins
  coinSize = 20
  coinAnimate = Animate('coin') #Coin animation 

  #Reset sheeps and coins based on the level
  sheeps, coins = reset(level)
  #Load images for GUI elements
  guiCoin = pygame.image.load('assets\coin.png')
  guiSack = pygame.image.load('assets\sack.png')
  guiSack = pygame.transform.scale(guiSack, (14,14)) #Scale the size of the sack image

  #-------------------------
  #       FARMER
  #-------------------------
  #Set the size of user
  userSizeX = 38
  userSizeY = 38
  defaultSpeed = 1
  #Set the intial spawn position of the user
  spawnX = 50
  spawnY = 50
  #Create a player object with the specified attributes
  user = Player([spawnX,spawnY],defaultSpeed,[width,height],userSizeX,userSizeY,3,obstImages,obstacles)
  #Create a mask for the user using an image file
  userMask = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets/farmerRun/Hobbit - run7.png"),(38,38)))
  #Create animations for the user's death, running and stopping
  farmDie = Animate('farmDie')
  farmRun = Animate('farmRun')
  farmStop = Animate('farmStop')

  #home
  homeImg = pygame.image.load("assets/house.png")
  homeImg = pygame.transform.scale(homeImg, (40,40))
  homeRect = pygame.Rect(10,10,40,40)

  #set up the assets for level 3 with alien rays
  if level == 3:
    #Load and scale the image for alien rays 
    buildImg = pygame.image.load("assets/caution1.png")
    buildImg = pygame.transform.scale(buildImg, (50,50))
    #Create a custom event for the alien event
    alienEvent = pygame.USEREVENT+1
    pygame.time.set_timer(alienEvent, 4900)
  #Set up the smoke animation
  smokeW = 50
  smokeH = 50
  smoke = Animate('smoke')

  #win/lose
  winImg = pygame.image.load('assets/win.png')
  winImg = pygame.transform.scale(winImg, (width, height))


  #---------------------------------
  #              SOUND
  #---------------------------------
  coinSound = pygame.mixer.Sound('assets/sounds/coin.mp3')
  coinSound.set_volume(0.2)
  packSheepSound = pygame.mixer.Sound('assets/sounds/sheep_baa.ogg')
  music = pygame.mixer.music.load('assets/sounds/backtrack.wav')
  pygame.mixer.music.play(-1)
  #coinSound = sound.SoundPlay('coin')
  loseImg = pygame.image.load('assets/lose.png')
  loseImg = pygame.transform.scale(loseImg, (width, height))

  #---------------------------------
  #          SOUND/MUSIC
  #---------------------------------
  #Create sound objects for different sounds
  coinSound = Sound('coin')
  packSheepSound = Sound('sheep')
  alarmSound = Sound('alarm')
  alienSmoke = Sound('alienSmoke')
  hitSound = Sound('hit')
  #Create music objects for different music tracks
  level1M = Music('level1')
  level2M = Music('level2')
  level3M = Music('level3')
  menuMusic = Music('menu')
  #Play specific music based on current level
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
  pygame.mouse.set_visible(False)
  while running:
    timer += 1
    # clock.tick(60)
    dt = clock.tick()
    #------------
    #INPUT
    #------------
    for event in pygame.event.get(): #Iterate through all pygram events
      if event.type == QUIT: #If the event is quitting the game
        #quit game
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN: #If a key is pressed
        #key pressed
        if event.key == K_r: #If the pressed key is 'r'
          #'r' to reset
          user.setPos([spawnX,spawnY])#Set the player's position to a spawn position
          #Resets the score, money, sacked count, sprint value,timer, and health values
          score = 0
          money = 0
          sacked = 0
          sprint = 1000
          timer = 0
          user.changeHealth([3])
          sheeps, coins = reset(level) #reset the sheeps and coins based on level
          if level == 3:
            #If level is 3 rest the rays and alien events
            numRay = 1
            nRI = 0
            timeSince = 0
            pygame.time.set_timer(alienEvent, 0)
            pygame.time.set_timer(alienEvent, 4900)
            rays = []
            buildUp = []
        elif event.key == K_ESCAPE: #If pressed key is escape key
          controller.normalWindow("LevelSelect") #Change the window to the level select screen
          return
      if level == 3 and event.type == alienEvent:
        buildUp = abduct(numRay,50,[width,height])
    # ----------
    # ALIEN RAYS
    # ----------
    if buildUp or rays:
      #Increase the time since the last event
      timeSince += clock.get_rawtime()
    if buildUp and timeSince >= 950:
      #Assign the buildUp to rays and reset buildUp and timeSince
      rays = buildUp
      buildUp = []
      timeSince = 0
    if rays and timeSince >= 1600:
      #Increment the number of ray iterations
      nRI += 1
      # Reset the number of ray iterations if it exceeds numRay*2
      if nRI == numRay*2:
        nRI = 0
        numRay += 1
      rays = []
      timeSince = 0
      
    # ------------------
    # CHARACTER MOVEMENT
    # ------------------
    pressed = pygame.key.get_pressed()
    if lifeStatus != False:
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
      if pressed[K_LSHIFT] and sprint > 0:
        # Increase the user's speed, decrease sprint energy, and set stop to False
        user.setSpeed(sprintSpeed*dt)
        sprint -= 5
        stop = False
      else:
        # Set the user's speed to the walk speed multiplied by dt (time since last frame)
        user.setSpeed(walkSpeed*dt)
      if pressed[K_h]:
        user.setSpeed(2)
        sackMax = 3
      if not pressed[K_RIGHT] and not pressed[K_d] and not pressed[K_LEFT] and not pressed[K_a] and not pressed[K_DOWN] and not pressed[K_s] and not pressed[K_UP] and not pressed[K_w]:
        stop = True
      if sprint < 1000:
        sprint += sprintGen*dt

    #win conditions
    if not sheeps and home:
      win = True
      running = False

    # ------
    # OUTPUT
    # ------
    # BACKGROUND
    screen.blit(grass, (0,0))
    #Create a rectangle representing the farmer's position
    farmerRect = pygame.Rect(user.getPos()[0], user.getPos()[1], userSizeX, userSizeY)
    # SHEEP
    for s in sheeps:
      current = pygame.Rect(s[0],s[1],sheepSzX,sheepSzY)
      #Display the sheep image based on its direction
      if s[2]:
        screen.blit(sheepFlipped,(current[0],current[1]))
      else:
        screen.blit(sheepImage,(current[0],current[1]))
      #Check if sheep have been sacked by user
      if current.colliderect(farmerRect) and sacked < sackMax:
        packSheepSound.playSound()
        sheeps.remove(s)
        sacked += 1
        score += 50
    # COINS
    for c in coins:
      coinAnimate.draw(screen,c[0],c[1], coinSize, coinSize,False, False)
      coinAnimate.update()
      #Check if coin has been collected by farmer
      if c.colliderect(farmerRect):
        coinSound.playSound()
        coins.remove(c)
        money += 1
        score += 10
    if level != 1:
      #horizontal wolves
      for w in wolfHorz:
        #Determine the direction of the wolf
        if w[0][0] >= w[1][1]:
          horzDirection = "left"
        if w[0][0] <= w[1][0]:
          horzDirection = "right"
        #Move the wolf and update animation based on direction
        if horzDirection == "right":
          wolfR.draw(screen, w[0][0], w[0][1], wolfW, wolfH, False, False)
          w[0][0] += 1
          wolfR.update()
        #Wolf run left
        else:
          wolfR.draw(screen, w[0][0], w[0][1], wolfW, wolfH, True, False)
          w[0][0] -= 1
          wolfR.update()
        #Check if wolf collides with the farmer and the farmer has remaining lives
        if wolfMaskHorz.overlap(userMask, (w[0][0]-user.getPos()[0],w[0][1]-user.getPos()[1])) and lifeStatus:
          user.changeHealth()
          lifeStatus = False

      #vertical wolves
      for w in wolfVert:
        #Check if the y-coordinate of the wolf is greater than or equal to 450
        if w[1] >= 450:
          vertDirection = "up"
        # Check if the y-coordinate of the wolf is less than or equal to 180
        if w[1] <= 180:
          vertDirection = "down"
        # Move the wolf vertically based on the vertDirection value
        if vertDirection == "down":
          wolfF.draw(screen, w[0], w[1], wolfVW, wolfVH, False,False) # Draw the wolf facing downwards
          w[1]+= 1
          wolfF.update()
        else:
          wolfB.draw(screen, w[0], w[1], wolfVW, wolfVH, False, False) # Draw the wolf facing upwards
          w[1]-= 1
          wolfB.update()
        # Check if the wolf's vertical mask overlaps with the user's mask and the lifeStatus is True
        if wolfMaskVert.overlap(userMask, (w[0]-user.getPos()[0],w[1]-user.getPos()[1])) and lifeStatus:
          user.changeHealth()
          lifeStatus = False
    #----------- 
    # OBSTACLES
    #-----------
    for i in obstacles:
      toBlit = obstImages[i[4]] # Get the image associated with the obstacle
      screen.blit(toBlit,(i[0],i[1])) # Draw the obstacle image on the screen at the specified position
    #--------
    # HOUSE
    #--------
    screen.blit(homeImg,(10,10))
    if homeRect.colliderect(farmerRect):
      sacked = 0
      home = True
    else:
      home = False
    #-------
    # RAYS
    #------
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
    # ----------
    # CHARACTER
    #-----------
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
    #Farmer stop left facing
    if faceRight == False and stop == True and lifeStatus == True:
      farmStop.draw(screen, user.getPos()[0],user.getPos()[1],userSizeX, userSizeY,True, False)
      farmStop.update()
    #Farmer death animation
    if lifeStatus == False:
      farmDie.draw(screen, user.getPos()[0],user.getPos()[1],userSizeX, userSizeY,False, False)
      farmDie.update()
      # If the current frame index of the "farmDie" animation is 11 - only loop thorugh animation once
      if farmDie.getIndex() == 11:
        #Reset player and game stats
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
          # Stop the alien event timer and restart it after 4.9 seconds
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
  # print(timePenalty)
  #Adjust the socre based on conditions
  if score >= timePenalty:
    score -= timePenalty
  elif win:
    score = 10
  else:
    score = 0
  #Update game statistics and level progress if player wins
  if win:
    with open('game/stats.txt','r') as textFile:
      file_content = textFile.readlines()
      infoLine = list(map(float,file_content[0].split()))
      infoLine[2] = money
      if infoLine[0] == level and infoLine[0] != 3:
        infoLine[0] += 1
    with open('game/stats.txt','w') as outFile:
      outText = ""
      for i in infoLine:
        outText += str(i) + " "
      outText += "\nlevel walkSpeed money sackMax sprintGen"
      outFile.write(outText) 
    #Check if player acheieved a top score
    scoreLoc = 'game/scores/lvl'+str(level)+'.txt'
    with open(scoreLoc,'r') as textFile:
      scoresInfo = textFile.readlines()
      topScores = scoresInfo[0].split()
      topNames = scoresInfo[1].split()
    for s in topScores:
      if score > int(s):
        #Display a text input box for the player to enter their username
        crownImg = pygame.transform.scale(pygame.image.load("assets/crown.png"),(50,50))
        pygame.mouse.set_visible(True)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        font = pygame.font.Font(None, 36)
        inputBox = pygame.Rect(150, 232, 200, 36)
        boxCol = (170,170,170) #(140,180,200)
        active = False
        username = ""
        submitted = False
        while not submitted:
          for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if inputBox.collidepoint(event.pos):
                active = True
              else:
                active = False
              boxCol = (40,80,120) if active else (170,170,170)
            if event.type == pygame.KEYDOWN and active:
              if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
              elif event.key == pygame.K_RETURN:
                submitted = True
              elif len(username) < 8 and event.key != pygame.K_SPACE:
                username += event.unicode
          #Display the input box and other UI elements
          screen.fill((200,200,180))
          screen.blit(crownImg, (225, 100))
          txtSurface = font.render(username, True, boxCol)
          screen.blit(txtSurface, (inputBox.x+5, inputBox.y+5))
          pygame.draw.rect(screen, boxCol, inputBox, 2)
          genText(screen,"New Top Score!",(240,200,80),(180,250),"middle",40)
          genText(screen,"Username:",(30,30,30),(220,250),"middle")
          pygame.display.update()
        #If no username is entered set a default username
        if username.strip() == "":
          username = "ANON"
        #Insert the new score and username into the top scores list
        topScores.insert(topScores.index(s),score)
        topNames.insert(topScores.index(s)-1,username)
        topScores.pop()
        topNames.pop()
        break
    #Update the top scores file with the modified scores and names
    with open(scoreLoc,'w') as outFile:
      outFile.write(f"{topScores[0]} {topScores[1]} {topScores[2]} {topScores[3]} {topScores[4]}\n{topNames[0]} {topNames[1]} {topNames[2]} {topNames[3]} {topNames[4]}")
  #Load and scale the back button image
  backButton = pygame.transform.scale(pygame.image.load("assets/back.png"),(96,44))
  backRect = pygame.Rect(202,398,96,44)

  #level cleared
  pygame.mouse.set_visible(True) #Make the mouse visible
  #Main loop for the "win state"
  while win:
    #Event handling loop
    for event in pygame.event.get():
      if event.type == QUIT:
        #quit game
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONUP and backRect.collidepoint(pygame.mouse.get_pos()): 
        #If the back button is clicked go to the level select screen
        controller.normalWindow("LevelSelect")
        return
    #Check if the mouse is over the back button and set the cursor accordingly
    if backRect.collidepoint(pygame.mouse.get_pos()):
      pygame.mouse.set_cursor(*pygame.cursors.diamond)
    else:
      pygame.mouse.set_cursor(*pygame.cursors.arrow)
    #Draw the win image on screen
    screen.blit(winImg, (0,0))
    #Display score text on screen
    genText(screen,"Score: " + str(score), (0,0,0), [300,250], "middle")
    match level:
      #Different cases to assign/rate the players performance 
      case 1:
        if score >= 450:
          stars = 3
        elif score >= 400:
          stars = 2
        elif score >= 350:
          stars = 1
        else:
          stars = 0
      case 2:
        if score >= 400:
          stars = 3
        elif score >= 350:
          stars = 2
        elif score >= 300:
          stars = 1
        else:
          stars = 0
      case 3:
        if score >= 450:
          stars = 3
        elif score >= 325:
          stars = 2
        elif score >= 250:
          stars = 1
        else:
          stars = 0
    for i in range(stars):
      #Diplay stars on screen based on number of stars earned
      screen.blit(starImg, (190+i*45,320))
    screen.blit(backButton,backRect)

    pygame.display.update()

  while not win:
    for event in pygame.event.get():
      if event.type == QUIT:
        #quit game if user closes window
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONUP and backRect.collidepoint(pygame.mouse.get_pos()):
        controller.normalWindow("LevelSelect")#Return to level select screen when the back button is clicked
        return
    if backRect.collidepoint(pygame.mouse.get_pos()):
      pygame.mouse.set_cursor(*pygame.cursors.diamond) # Change the mouse cursor to a diamond shape when hovering over the back button
    else:
      pygame.mouse.set_cursor(*pygame.cursors.arrow) # Change the mouse cursor to an arrow shape when not hovering over the back button
    screen.blit(loseImg, (0,0))
    genText(screen,"Score: " + str(score), (250,250,250), [380,250], "middle")
    screen.blit(backButton,backRect)
    pygame.display.update()

# startLevel(2)