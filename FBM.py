from random import randint
from typing import Text
import pygame
from pygame.locals import *
import time
import pygame as pg
import random
pygame.init()
pygame.font.init()
clock=pygame.time.Clock()
fps=60

screen_width1 = 600
screen_height1 = 600

screen1 = pygame.display.set_mode((screen_width1, screen_height1))
pygame.display.set_caption('Flying Bandit Maze')

def draw(self, screen1):
        # Blit the text.
        screen1.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen1, self.color, self.rect, 2)

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


def right_answer():
	print('correct')
	
def wrong_answer():
	print('wrong')
	




#background image
game_bg=pygame.image.load('images/878.jpg')
#defines grid so later I can assign blocks to them
tile_size=60
def draw_grid():
	for line in range(0, 10):
		pygame.draw.line(screen1, (255, 255, 255), (0, line * tile_size), (screen_width1, line * tile_size))
		pygame.draw.line(screen1, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height1))
class Player():
	def __init__(self, x, y):
		img = pygame.image.load('images/player.png')
		self.image = pygame.transform.scale(img, (30, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False

	def update(self):
		dx = 0
		dy = 0
		end_run = lambda: 0

		#controls
		key = pygame.key.get_pressed()
		if key[pygame.K_UP] and self.jumped == False:
			self.vel_y = -6
			self.jumped = True
		if key[pygame.K_SPACE] == False:
			self.jumped = False
		if key[pygame.K_LEFT]:
			dx -= 5
		if key[pygame.K_RIGHT]:
			dx += 5

		#add gravity
		self.vel_y += 1
		if self.vel_y > 5:
			self.vel_y = 5
		dy += self.vel_y

		#check for collision
		for tile in world.tile_list:
			#check for collision in x direction
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			#check for collision in y direction
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground i.e. jumping
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				#check if above the ground i.e. falling
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0

        

        #check for collision with chests
			
			if key[pygame.K_DOWN] and pygame.sprite.spritecollide(self, Question_block, False):
				d=random.randint(11,99)
				x=random.randint(11,99)
				z=d+x
				c=int(input('What is {}+{}?'.format(d,x)))
				if c ==(z):
					print(right_answer)
					break		
				else:
					print(wrong_answer)
					break
			if key[pygame.K_DOWN] and pygame.sprite.spritecollide(self, Question_block2, False):
				d=random.randint(1,10)
				x=random.randint(1,10)
				z=d*x
				c=int(input('What is {}*{}?'.format(d,x)))
				if c ==(z):
					right_answer
					break
				else:
					wrong_answer
					break
			if key[pygame.K_DOWN] and pygame.sprite.spritecollide(self, Question_block3, False):
				d=random.randint(21,99)
				x=random.randint(1,20)
				z=d-x
				c=int(input('What is {}-{}?'.format(d,x)))
				if c ==(z):
					right_answer
				else:
					wrong_answer
					break
			if pygame.sprite.spritecollide(self, doorforescape, False):
			 
				font=pygame.font.Font('freesansbold.ttf',32)
				text1=font.render("YOU MANAGED TO ESCAPE!!",True,(0,225,0))
				screen1.blit(text1,(22,0))
	

		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > screen_height1:
			self.rect.bottom = screen_height1
			dy = 0

		#draw player onto screen
		screen1.blit(self.image, self.rect)
		end_run()
		


#For addition questions
class Questionblock(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/chest.jpg')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y	
#For multiplication questions
class Questionblock2(Questionblock):
	pass
	
#For subtraction questions
class Questionblock3(Questionblock):
	 pass
class escapedoor(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/door.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		stone_img = pygame.image.load('images/stone.jpg')
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(stone_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
			    
				if tile == 3:
					Question=Questionblock(col_count * tile_size +10, row_count * tile_size +40)
					Question_block.add(Question)
				if tile == 4:
					Question2=Questionblock2(col_count * tile_size +10, row_count * tile_size +40)
					Question_block2.add(Question2)
				if tile == 5:
					Question3=Questionblock3(col_count * tile_size +10, row_count * tile_size +40)
					Question_block3.add(Question3)
				if tile == 6:
					door=escapedoor(col_count * tile_size +10, row_count * tile_size -12)
					doorforescape.add(door)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen1.blit(tile[0], tile[1])

        
#The grid for which to assign different blocks to places in window

world_data=[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,4,0,0,0,1],
[1,0,0,1,1,1,0,6,0,1],
[1,5,0,0,0,1,1,1,1,1],
[1,1,0,0,0,0,0,0,0,1],
[1,0,1,1,4,0,0,0,0,1],
[1,0,0,0,1,1,1,1,0,1],
[1,0,0,0,0,3,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1],
]
Question_block= pygame.sprite.Group()

Question_block2= pygame.sprite.Group()

Question_block3= pygame.sprite.Group()

doorforescape= pygame.sprite.Group()

world= World(world_data)
player = Player(100, screen_height1 - 130)


run = True
while run:
	
	
    clock.tick(fps)
    screen1.blit(game_bg,(1,1))
    
    world.draw()

    player.update()
	
	
    Question_block.update()
    Question_block.draw(screen1)
	
    
    Question_block2.update()
    Question_block2.draw(screen1)
    
    Question_block3.update()
    Question_block3.draw(screen1)
    
    doorforescape.update()
    doorforescape.draw(screen1)
	

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
         
