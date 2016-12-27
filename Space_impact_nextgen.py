# Bond_007 productions
# Space Impact Nextgen :-) Game !
# this game is made for fun purpose only, any sought of resemblence with copy-write protected games is purely intentional :p
# Actually the game is designed developed with the help from youtube channel,
# and it's my first game
''' don't change the display_width and display_height because most of the
enemy dimension are w.t.t 800*600 only ! '''

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
car_width = 200
car_height = 200
# Colours definition :
black = (0,0,0)# RGB absence of all colours
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,100,255)
tab = (150,255,0)
background = (255,255,130)
game_background = (80,240,200)
corner = (200,100,0) 

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Impact - Nextgen. !')
clock = pygame.time.Clock()

carImg = pygame.image.load('space_impact_user.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def score(count):
    font = pygame.font.Font('ITCBLKAD.ttf',30)
    text = font.render("Score : "+str(count),True,white)
    gameDisplay.blit(text,(10,10))

def enemy(enemyx,enemyy,enemyw,enemyh,color):
    pygame.draw.rect(gameDisplay,color,[enemyx,enemyy,enemyw,enemyh])
    
    
def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text,size,t):
    largeText = pygame.font.Font('CHILLER.ttf',size)
    textsurf,textrect = text_objects(text,largeText)
    textrect.center = ((display_width/2),(display_height/2)-50)
    gameDisplay.blit(textsurf,textrect)
    if t == 2:
        pygame.display.update()
        time.sleep(t)
        game_loop()
    elif t == 1:
        time.sleep(t)
    
def crash():
    message_display('You crashed !',115,2)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(background)
        message_display('Space Impact - Nextgen !',100,5)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 450+250 > mouse[0] > 450 and 450+90 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay,tab,(450,450,250,90))
            #game_loop()
            #print (event)
            if click[0] == 1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(450,450,250,90))
        smallText = pygame.font.Font('HARNGTON.ttf',30)
        textsurf,textrect = text_objects('Wanna Play !',smallText)
        textrect.center = ((450+125),(450+45))
        gameDisplay.blit(textsurf,textrect)
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textsurf,textrect = text_objects('Developed by : Bond_007',smallText)
        textrect.center = (400,580)
        gameDisplay.blit(textsurf,textrect)
        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    x = (display_width*0-90)
    y = (display_height*0.30)
    y_change = 0
    enemy_startx = 800
    enemy_starty = random.randrange(0,display_height)
    enemy_startw = 80
    enemy_starth = 80
    enemy_speed = -10
    enemy_accleration = 0.3
    count = 0
    gameExit= False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5

            y+=y_change

        gameDisplay.fill(game_background)        
        car(x,y)
        enemy(enemy_startx,enemy_starty,enemy_startw,enemy_startw,blue)
        enemy_startx+=enemy_speed
        pygame.draw.rect(gameDisplay,corner,(0,0,800,67))
        pygame.draw.rect(gameDisplay,corner,(0,500,800,100))
        score(count)
        if y < 0 or y > display_height-car_height:
                crash()
        if enemy_startx < 0:
            enemy_startx = 800
            enemy_starty = random.randrange(80,display_height-120)
            enemy_speed-=enemy_accleration
            enemy_starth+=enemy_accleration*5
            count+=1
        if enemy_startx <= 90:
            if y+80   > enemy_starty and y+90 < enemy_starty+enemy_starth:
                enemy(enemy_startx,enemy_starty,enemy_startw,enemy_startw,green)
                crash()
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
