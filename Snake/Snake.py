import sys
import random
import pygame as pg
import pyautogui as gui



def run_game(counttime):
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
				if event.key == pg.K_ESCAPE:
					sys.exit()
				elif event.key == pg.K_RIGHT:
					finalMove = 1
				elif event.key == pg.K_UP:
					finalMove = 2
				elif event.key == pg.K_LEFT:
					finalMove = 3
				elif event.key == pg.K_DOWN:
					finalMove = 4
		screen.fill((0,0,0))
		if count % counttime == 0:
			snake.changeDirection(finalMove)
			food.draw(screen)
			if snake.position == food.position:
				food.generate(snake.positions)
				snake.updateLength(screen, food)
			else:
				snake.update(screen, False, food)
			pg.display.flip()
		count+=1

def reset(snake, food):
	snake.position = (5, 5)
	snake.positions = []
	snake.direction = 1
	gui.press('right')
	snake.length = 1
	food.generate(snake.positions)

class Snake():
	def __init__(self):
		self.position = (5, 5)
		self.positions = []
		self.dimension = (20, 20)
		self.direction = 1
		self.length = 1
	def changeDirection(self, direction):
		if not (self.direction - direction) % 2 == 0:
			self.direction = direction
	def updateLength(self, screen, food):
		self.length+=1
		if self.length == 900:
			reset(self, food)
		self.update(screen, True, food)
	def update(self, screen, new, food):
		if new == False and self.positions:
			self.positions.pop(0)
		if self.direction == 1:
			self.position = ((self.position[0]+25), (self.position[1]))
		elif self.direction == 2:
			self.position = ((self.position[0]), (self.position[1]-25))
		elif self.direction == 3:
			self.position = ((self.position[0]-25), (self.position[1]))
		elif self.direction == 4:
			self.position = ((self.position[0]), (self.position[1]+25))
		pg.draw.rect(screen, (255,255,255), (self.position[0], self.position[1], 20, 20))
		for pos in self.positions:
			pg.draw.rect(screen, (255,255,255), (pos[0], pos[1], 20, 20))
		if self.position[0] < 0 or self.position[0] > 751 or self.position[1] < 0 or self.position[1] > 751:
			reset(self, food)
		for pos in self.positions:
			if self.position == pos:
				reset(self, food)
		self.positions.append(self.position)

class Food:
	def __init__(self):
		self.position = ((random.randint(5, 24) * 25) + 5, (random.randint(5, 24) * 25) + 5)
	def generate(self, positions):
		x = random.randint(0, 29)
		y = random.randint(0, 29)
		self.position = ((x * 25) + 5, (y * 25) + 5)
		for pos in positions:
			if pos == self.position:
				self.generate(positions)
	def draw(self, screen):
		pg.draw.rect(screen,(168, 18, 18),(self.position[0],self.position[1],20,20))

run_game(1000.0)

if __name__ == "__main__":	
	main()