import pygame
from pygame.locals import *

import characters

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


grass = pygame.image.load("assets\grass-588.jpg")
grass = pygame.transform.scale(grass, (500,500))


obstacles = [[0,100,50,50],[250,0,50,50],[250,150,50,50],[50,200,50,50],[150,300,50,50],[400,150,50,50],[350,400,50,50]]
defaultPos = [50,50]
userSize = 30
user = characters.Player(defaultPos,0.2,[width,height],userSize,obstacles)
charImg = pygame.image.load("assets\char.png").convert()
charImg = pygame.transform.scale(charImg, (userSize,userSize))

sheep = [characters.Sheep([260,380]),characters.Sheep([130,180]),characters.Sheep([420,70])]

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_r:
            user.setPos(defaultPos)
        elif event.type == QUIT:
            pygame.quit()
    screen.blit(grass, (0, 0))
    screen.blit(charImg, (user.getPos()[0],user.getPos()[1]))

    pressed = pygame.key.get_pressed()
    if pressed[K_RIGHT] or pressed[K_d]:
        user.moveRight()
    elif pressed[K_LEFT] or pressed[K_a]:
        user.moveLeft()
    elif pressed[K_DOWN] or pressed[K_s]:
        user.moveDown()
    elif pressed[K_UP] or pressed[K_w]:
        user.moveUp()
    elif pressed[K_r]:
        user.setPos(defaultPos)

    for i in obstacles:
        obst = pygame.Rect(i[0],i[1],i[2],i[3])
        pygame.draw.rect(screen,(80,40,10),obst)
    
    for i in sheep:
        if i.getState() == False:
            pygame.draw.circle(screen,(250,250,250),i.getPos(),15)
        i.claim(user.getMid())
    
    pygame.display.update()