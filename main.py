import pygame, sys
from pygame.locals import QUIT
import random
import time
import math

pygame.init()

screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption('Apple Game')
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 125
playerY = 450
playerX_change = 0
playerY_change = 0.1
ufo = pygame.transform.scale(playerImg, (50, 50))

# Enemy
enemyImg = pygame.image.load('cow.png')
enemyX = random.randrange(0, 300)
enemyY = 300
enemyX_change = 0.3
enemyY_change = 0
cow = pygame.transform.scale(enemyImg, (50, 50))

width = 65
height = 130

vel = 0.5

def enemy(x, y):
    screen.blit(cow, (enemyX, enemyY)) 

def player(x, y):
    screen.blit(ufo, (playerX, playerY))
  
userInput = pygame.key.get_pressed()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerX > vel:
      playerX -= vel 
      
    if keys[pygame.K_RIGHT] and playerX < 300 - width - vel :
      playerX += vel 
      
    #if keys[pygame.K_UP] and playerY > vel:
      playerY -= vel
      
    #if keys[pygame.K_DOWN] and playerY < 600 - height - vel: 
      playerY += vel
      
    screen.fill((255 ,255, 255))
    
    playerY += playerY_change
    
    if playerY <= 0:
        playerY_change = 0.1
    elif playerY >= 536:
        playerY_change = -0.1
        
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 0.3
    elif enemyX >= 236:
        enemyX_change = -0.3

    player(playerX, playerY)
    enemy(enemyX, enemyY)
  
    pygame.display.update() 
