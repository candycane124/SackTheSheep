import pygame, sys
from pygame.locals import *
import entity
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Pixel Perfect')

#obstacles
obstacles = [
    [0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]
]
obstImages = []
imageLinks = ["assets/obstacles/x0.png","assets/obstacles/x1.png","assets/obstacles/x2.png","assets/obstacles/3.png","assets/obstacles/4.png","assets/obstacles/5.png"]
for i in imageLinks:
  obstImage = pygame.image.load(i)
  obstImage = pygame.transform.scale(obstImage, (50,50))
  obstImages.append(obstImage)
for i in obstacles:
  i.append(random.randint(0,len(imageLinks)-1))

#player
userSizeX, userSizeY = 38, 38
animationImg = pygame.transform.scale(pygame.image.load('assets/farmerRun/Hobbit - run1.png'),(userSizeX, userSizeY))
currentMask = pygame.mask.from_surface(pygame.transform.scale(pygame.image.load("assets/farmerRun/Hobbit - run7.png"),(userSizeX,userSizeY)))
# user = entity.Player([50,50],0.5,[WIDTH,HEIGHT],userSizeX,userSizeY,obstacles)

COL = (0,0,0)
masked = False
while True:
    clock.tick(100)
    screen.fill(COL)

    for event in pygame.event.get():
        if event.type == QUIT:
            #quit game
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_m:
                masked = not masked

    mx, my = pygame.mouse.get_pos()
    if masked:
        screen.blit(currentMask.to_surface(), (mx, my))
    else:
        screen.blit(animationImg, (mx, my))

    screen.blit(animationImg, (mx,my))
    for i in obstacles:
        toBlit = obstImages[i[4]]
        obstMask = pygame.mask.from_surface(toBlit)
        screen.blit(toBlit,(i[0],i[1]))
        if currentMask.overlap(obstMask,(i[0]-mx,i[1]-my)):
            COL = (250,250,250)
        else:
            COL = (0,0,0)

    pygame.display.update()


#1 0.5 0.6 0 1 1
#level walkSpeed sprintSpeed money sackMax sprintGen