import pygame, sys
from pygame.locals import *

class Item():
      def __init__(self,assetLocation,alphaChannel,size,position,cost,description,ability):
          self.image = pygame.transform.scale(pygame.image.load(assetLocation),size)
          if alphaChannel:
            self.image.set_colorkey((255,255,255))
          self.rect = self.image.get_rect(center=position)
          self.mask = pygame.mask.from_surface(self.image)
          self.cost = cost
          self.description = description
          self.ability = ability
      def __str__(self):
          return f"{self.description}, costs {self.cost} and results in {self.ability}"

def genText(screen, txt, colour, pos, posType, fontSize=12):
    '''
    Blit's text to screen
    Parameters
    -----
    screen

    txt : Str
      Text that will be displayed
    colour : int ( )
      RGB colour of text
    pos : int [ ]
      y, x position of text
    posType : Str
      "top-right", "bottom-left", "bottom-right", "top-left", or "middle"
    fontSize : int
      Font size of text, default 12
    '''
    font = pygame.font.Font('freesansbold.ttf', fontSize)
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

def shop():
  pygame.init()
  width, height = 500, 500
  screen = pygame.display.set_mode((width, height))
  clock = pygame.time.Clock()
  pygame.display.set_caption('Pixel Perfect')

  with open('game/stats.txt','r') as textFile:
    file_content = textFile.readlines()
    info = list(map(float,file_content[0].split()))

shop = []
raw = []
with open('game/shop_items.txt','r') as textFile:
  file_content = textFile.readlines()
  for i in file_content:
    raw.append(i)
    itemData = i.split(",")
    shop.append(Item(itemData[0],itemData[1]=="True",(int(itemData[2]),int(itemData[3])),(int(itemData[4]),int(itemData[5])),int(itemData[6]),itemData[7],[int(itemData[8]),float(itemData[9])]))
   
# shop = [
#     Item("assets/shop/sack.png",False,(70,70),(120,210),3,"Better Sack: Carry up to 2 sheeps at a time!",[3,1]),
#     Item("assets/shop/shoe.png",False,(78,64),(220,310),2,"Speedy Spurs: Increases your walking and running speed!",[1,0.1]),
#     Item("assets/shop/temp_pot.png",True,(60,60),(410,230),2,"Magic Mana: Improve your sprint regeneration!",[4,0.5])
# ]

  #back
  backPos = 15
  backSize = 30
  backImg = pygame.transform.scale(pygame.image.load("assets/shop/back.png"),(backSize,backSize))
  backRect = pygame.Rect(backPos,backPos,backSize,backSize)

  #cursor
  cursorImg = pygame.transform.scale(pygame.image.load("assets/shop/cursor.png"),(15,16))
  grabImg = pygame.transform.scale(pygame.image.load("assets/shop/cursor_grab.png"),(15,16))
  pygame.mouse.set_visible(False)

  guiCoin = pygame.image.load('assets\coin.png')

  background = pygame.image.load('assets/shop/cart.png')

  black = (10,10,10)
  white = (250,250,250)
  timer = 0
  timer2 = 0
  buyTimer = False
  errTimer = False
  running = True
  while running:
    clock.tick(100)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
      if event.type == QUIT:
        #quit game
        pygame.quit()
        sys.exit()

    currentCursor = cursorImg
    mousePos = pygame.mouse.get_pos()
    for i in shop:
      posInMask = (mousePos[0]-i.rect.x,mousePos[1]-i.rect.y)
      if i.rect.collidepoint(*mousePos) and i.mask.get_at(posInMask):
        currentCursor = grabImg
        genText(screen,str(i.cost) + " coin(s) | " + i.description,black,(490,10),"bottom-left",12)
        if pygame.mouse.get_pressed()[0]:
          if info[2] >= i.cost:
            info[2] -= i.cost
            raw.pop(shop.index(i))
            shop.remove(i)
            info[i.ability[0]] += i.ability[1]
            with open('game\stats.txt','w') as outFile:
              newStats = ""
              for j in info:
                newStats += str(j)
                # if j != info[-1]:
                newStats += " "
              newStats += "\nlevel walkSpeed money sackMax sprintGen"
              outFile.write(newStats)
            buyTimer = True
          else:
            errTimer = True
      screen.blit(i.image, i.rect)
    
    if buyTimer:
      timer += clock.get_rawtime()
    if buyTimer and timer <= 1500:
      genText(screen,"Purchase Successful!",black,(250,250),"middle",24)
    elif buyTimer and timer > 1500:
      buyTimer = False
      timer = 0

    if errTimer:
      timer2 += clock.get_rawtime()
    if errTimer and timer2 <= 1200:
      pygame.draw.rect(screen,(245,245,245),(345,40,145,35))
      genText(screen,"Error: Not enough coins",(160,40,25),(45,350),"top-left")
      genText(screen,"to purchase this item.",(160,40,25),(60,350),"top-left")
    elif errTimer and timer2 > 1200:
      errTimer = False
      timer2 = 0

    #back button
    screen.blit(backImg,(backPos,backPos))
    if pygame.mouse.get_pressed()[0] and backRect.collidepoint(pygame.mouse.get_pos()):
      running = False

    #coin
    screen.blit(guiCoin, (472,14))
    genText(screen,str(int(info[2])),(255,195,0), [25,456], "middle",20)

    #mouse
    screen.blit(currentCursor,mousePos)
    
    pygame.display.update()


with open('game/shop_items.txt','w') as outFile:
    remainingItems = ""
    for i in raw:
      outFile.write(i)

shop()