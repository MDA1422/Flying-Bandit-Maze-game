import pygame
from pygame.locals import *

pygame.init()

screen_width1 = 768
screen_height1 = 548

screen1 = pygame.display.set_mode((screen_width1, screen_height1))
pygame.display.set_caption('MRG.intro')

game_intro=pygame.image.load('images/gameintro.jpg')
run = True
while run:
    screen1.blit(game_intro,(1,1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
         
