import pygame
from pygame.locals import *

pygame.init()

clock=pygame.time.Clock()
fps=60

screen_width1 = 600
screen_height1 = 600

screen1 = pygame.display.set_mode((screen_width1, screen_height1))
pygame.display.set_caption('MRG')

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
		self.vel_y = 0
		self.jumped = False

	def update(self):
		dx = 0
		dy = 0

		#controls
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
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

		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > screen_height1:
			self.rect.bottom = screen_height1
			dy = 0

		#draw player onto screen
		screen1.blit(self.image, self.rect)
        
        




class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		stone_img = pygame.image.load('images/stone.jpg')
		gate_img = pygame.image.load('images/gate.jpg')

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
				if tile == 2:
					img = pygame.transform.scale(gate_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen1.blit(tile[0], tile[1])
            

#The grid for which to assign different blocks to places in window
world_data=[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,0,1],
[1,0,0,0,0,2,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1],
]


world=World(world_data)
player = Player(100, screen_height1 - 130)

run = True
while run:
    clock.tick(fps)
    screen1.blit(game_bg,(1,1))
    world.draw()
    player.update()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
         
