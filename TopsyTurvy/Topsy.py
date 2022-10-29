from tkinter import font
import pygame
import math
import random

# initialzing pygame
pygame.init()


WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#player 
player_img = pygame.image.load('TopsyTurvy\data\player.png')
player_x = 390
player_y = 500
playerX_change = 0
playerY_change = 0

#coin  
coin_img = pygame.image.load('TopsyTurvy\data\coin.png')
coin_y = 250
coin_x = random.randint(0,700)

#enemy
enemy_img = pygame.image.load('TopsyTurvy\data\enemy.png')
enemy_x = coin_x
enemy_y = 0
enemyY_change = 0.02




#score
score_value = 0
font = pygame.font.Font('TopsyTurvy\\fonts\PEOPLE BOOK.otf', 30)
textX = 10
textY = 10




# Title and icon
pygame.display.set_caption("Topsy Turvy")
icon = pygame.image.load('TopsyTurvy\data\logo.png')
pygame.display.set_icon(icon)


#functions 
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def show_score(x,y):
    score = font.render("Coins: "+ str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def show_coin(x,y):
    screen.blit(coin_img, (x, y))


def isCollision(player_x, player_y, coin_x, coin_y): # calculation for the collision
    distance = math.sqrt(math.pow(player_x-coin_x, 2)) + (math.pow(player_y-coin_y, 2))
    if distance < 30:
        return True
    else:
        return False





#game loop
running = True
while running:

    #color off the screen
    screen.fill((230, 255, 255))

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_change = -0.06
                
            if event.key == pygame.K_a:
                playerX_change = 0.06
                
            if event.key == pygame.K_s:
                playerY_change = -0.06
                
            if event.key == pygame.K_w:
                playerY_change = 0.06
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                 playerX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                 playerY_change = 0
        

        

    player_x += playerX_change # player movement
    player_y += playerY_change # player movement
    enemy_y += enemyY_change # enemy movement

    # if statements
    if(player_x <= 0): # player cant go outside the screen
        player_x = 0
    if(player_x >= 770):
        player_x = 770
    if(player_y<=0):
        player_y = 0
    if (player_y>=570):
        player_y = 570

    
 
    #collison
    collision_coin_player = isCollision(player_x, player_y, coin_x, coin_y) # if player collide with the coin
    if collision_coin_player:
        score_value += 1
        enemy_x = random.randint(0, 700)
        enemy_y = 0
        coin_x = enemy_x 
        coin_y = random.randint(150, 500)

    collision_player_enemy = isCollision(player_x, player_y, enemy_x, enemy_y) # if enemy collide with player
    if collision_player_enemy:
        score_value = 0
        distance = 40
        player_x = random.randint(0, 700) 
        player_y = random.randint(50, 500)
        enemy_x = random.randint(0, 700)
        enemy_y = 0
        coin_x = enemy_x 
        coin_y = random.randint(150, 500)

    collision_coin_enemy = isCollision(enemy_x, enemy_y, coin_x, coin_y) # if enemy collide with enemy
    if collision_coin_enemy:
        score_value -= 1
        enemy_x = random.randint(0, 700)
        enemy_y = 0
        coin_x = enemy_x 
        coin_y = random.randint(150, 500)
        
    
    if(enemy_y >= 600):
        enemy_y = 0
        enemy_x = coin_x # enemy x spawns at the same x-value as coin x
    

    if(score_value <= 0): # score cant go lower then 0
        score_value = 0

    # for loops
    
       
    #calling the functions
    show_coin(coin_x, coin_y)
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score(textX, textY)
    
    
    pygame.display.update() 

    
