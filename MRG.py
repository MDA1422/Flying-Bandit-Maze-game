import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MRG')

 class platform(pygame.sprite.Sprite):
        
        

     #main menu
menu_img=pygame.image.load('img/sun')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quuit()
         
