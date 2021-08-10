import pygame
from pygame.locals import *

pygame.init()

screen_width1 = 600
screen_height1 = 600

screen1 = pygame.display.set_mode((screen_width1, screen_height1))
pygame.display.set_caption('MRG')

#images
game_bg=pygame.image.load('images/878.jpg')
#grid
tile_size=60
def draw_grid():
	for line in range(0, 10):
		pygame.draw.line(screen1, (255, 255, 255), (0, line * tile_size), (screen_width1, line * tile_size))
		pygame.draw.line(screen1, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height1))

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


world_data=[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1],
]

world=World(world_data)

run = True
while run:
    screen1.blit(game_bg,(1,1))
    world.draw()

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
         
