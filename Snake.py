import sys
import random
import pygame as pg

def run_game():
	pg.init()
	screen = pg.display.set_mode((1330, 755))
	pg.display.set_caption("Snake")
	snake = Snake()
	food = Food()
	count = 0.0
	finalMove = 1
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RIGHT:
					finalMove = 1
				elif event.key == pg.K_UP:
					finalMove = 2
				elif event.key == pg.K_LEFT:
					finalMove = 3
				elif event.key == pg.K_DOWN:
					finalMove = 4
		screen.fill((0,0,0))
		if count % 750.0 == 0:
			snake.changeDirection(finalMove)
			snake.update()
			food.draw(screen)
			snake.draw(screen)
			if snake.position == food.position:
				food.generate(snake.positions)
				snake.updateLength()
			pg.display.flip()
		count+=1

class Snake():
	def __init__(self):
		self.position = (5, 5)
		self.positions = [self.position]
		self.dimension = (20, 20)
		self.direction = 1
		self.length = 1
	def changeDirection(self, direction):
		if not (self.direction - direction) % 2 == 0:
			self.direction = direction
	def updateLength(self):
		self.length+=1
		if self.length == 1560:
			sys.exit()
		self.positions.append(self.position)
	def update(self):
		if self.direction == 1:
			self.position = ((self.position[0]+25) % 1325, (self.position[1]) % 750)
		elif self.direction == 2:
			self.position = ((self.position[0]) % 1325, (self.position[1]-25) % 750)
		elif self.direction == 3:
			self.position = ((self.position[0]-25) % 1325, (self.position[1]) % 750)
		elif self.direction == 4:
			self.position = ((self.position[0]) % 1325, (self.position[1]+25) % 750)
		if self.position[0] < 0 or self.position[0] > 1326 or self.position[1] < 0 or self.position[1] > 751
			sys.exit()
		for pos in self.positions:
			if self.position == pos:
				sys.exit()
		self.positions.append(self.position)
		self.positions.pop(0)
	def draw(self, screen):
		pg.draw.rect(screen, (255,255,255), (self.position[0], self.position[1], 20, 20))
		for pos in self.positions:
			pg.draw.rect(screen, (255,255,255), (pos[0], pos[1], 20, 20))

class Food():
	def __init__(self):
		self.position = (655, 380)
	def generate(self, positions):
		taken = False
		x = random.randint(0, 51)
		y = random.randint(0, 29)
		self.position = ((x * 25) + 5, (y * 25) + 5)
		for pos in positions:
			if pos == self.position:
				self.generate(positions)
			self.position = ((x * 25) + 5, (y * 25) + 5)
	def draw(self, screen):
		pg.draw.rect(screen,(168, 18, 18),(self.position[0],self.position[1],20,20))

run_game()