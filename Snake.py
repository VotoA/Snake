import sys
import random
import pygame as pg

def run_game():
	pg.init()
	screen = pg.display.set_mode((755, 755))
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
		if count % 1000.0 == 0:
			snake.changeDirection(finalMove)
			food.draw(screen)
			snake.draw(screen)
			if snake.position == food.position:
				food.generate(snake.positions)
				snake.updateLength()
			else:
				snake.update(False)
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
		if self.length == 900:
			sys.exit()
		self.update(True)
	def update(self, new):
		if self.position[0] < 0 or self.position[0] > 751 or self.position[1] < 0 or self.position[1] > 751:
			sys.exit()
		if self.direction == 1:
			self.position = ((self.position[0]+25), (self.position[1]))
		elif self.direction == 2:
			self.position = ((self.position[0]), (self.position[1]-25))
		elif self.direction == 3:
			self.position = ((self.position[0]-25), (self.position[1]))
		elif self.direction == 4:
			self.position = ((self.position[0]), (self.position[1]+25))
		for pos in self.positions:
			if self.position == pos:
				sys.exit()
		self.positions.append(self.position)
		if new == False:
			self.positions.pop(0)
		print(self.positions)
	def draw(self, screen):
		pg.draw.rect(screen, (255,255,255), (self.position[0], self.position[1], 20, 20))
		for pos in self.positions:
			pg.draw.rect(screen, (255,255,255), (pos[0], pos[1], 20, 20))

class Food():
	def __init__(self):
		self.position = (655, 380)
	def generate(self, positions):
		x = random.randint(0, 29)
		y = random.randint(0, 29)
		self.position = ((x * 25) + 5, (y * 25) + 5)
		for pos in positions:
			if pos == self.position:
				self.generate(positions)
	def draw(self, screen):
		pg.draw.rect(screen,(168, 18, 18),(self.position[0],self.position[1],20,20))

run_game()
