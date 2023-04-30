import pygame, sys
from pygame.locals import *

pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Pixel Perfect')

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

font = pygame.font.Font('freesansbold.ttf', 11)
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
    rendRect.center = (pos[1], pos[0])
  screen.blit(rendered,rendRect)

with open('main\stats.txt','r') as textFile:
  file_content = textFile.readlines()
  info = list(map(float,file_content[0].split()))
  # level = info[0]
  # walkSpeed = info[1]
  # money = int(info[2])
  # sackMax = int(info[3])
  # sprintGen = info[4]

shop = []
raw = []
with open('main/shop_items.txt','r') as textFile:
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

backPos = 15
backSize = 30
backImg = pygame.transform.scale(pygame.image.load("assets/red.png"),(backSize,backSize))
backRect = pygame.Rect(backPos,backPos,backSize,backSize)

guiCoin = pygame.image.load('assets\coin.png')


buyEvent = pygame.USEREVENT+1
black = (10,10,10)
white = (250,250,250)
timer = 0
startTimer = False
running = True
while running:
    clock.tick(100)
    screen.fill((white))

    for event in pygame.event.get():
      if event.type == QUIT:
          #quit game
          pygame.quit()
          sys.exit()
      elif event.type == buyEvent:
          pass

    mousePos = pygame.mouse.get_pos()
    for i in shop:
        posInMask = (mousePos[0]-i.rect.x,mousePos[1]-i.rect.y)
        if i.rect.collidepoint(*mousePos) and i.mask.get_at(posInMask):
            genText(i.description,black,(i.rect.y+i.rect.height+10,i.rect.x),"top-left")
            if pygame.mouse.get_pressed()[0]:
               if info[2] >= i.cost:
                  info[2] -= i.cost
                  raw.pop(shop.index(i))
                  shop.remove(i)
                  info[i.ability[0]] += i.ability[1]
                  with open('main\stats.txt','w') as outFile:
                      newStats = ""
                      for j in info:
                          newStats += str(j)
                          if j != info[-1]:
                            newStats += " "
                      newStats += "\nlevel walkSpeed money sackMax sprintGen"
                      outFile.write(newStats)
                  startTimer = True
        screen.blit(i.image, i.rect)
    
    if startTimer:
      timer += clock.get_rawtime()
    if startTimer and timer <= 2000:
      font = pygame.font.Font('freesansbold.ttf', 36)
      genText("Purchase Successful!",(240,200,20),(250,250),"middle")
      font = pygame.font.Font('freesansbold.ttf', 11)
    elif startTimer and timer > 2000:
      startTimer = False
      timer = 0
    

    screen.blit(backImg,(backPos,backPos))
    if pygame.mouse.get_pressed()[0] and backRect.collidepoint(pygame.mouse.get_pos()):
      running = False

    font = pygame.font.Font('freesansbold.ttf', 20)
    screen.blit(guiCoin, (472,14))
    genText(str(int(info[2])),(255,195,0), [20,460], "middle")
    font = pygame.font.Font('freesansbold.ttf', 11)

    pygame.display.update()


with open('main/shop_items.txt','w') as outFile:
    remainingItems = ""
    for i in raw:
      remainingItems += i
      if i != raw[-1]:
        remainingItems += "\n"
    outFile.write(remainingItems)