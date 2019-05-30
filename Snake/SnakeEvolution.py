import sys
import random
import math
import pygame as pg
import pyautogui as gui
import operator
import copy

def run_game(counttime, nNetwork, show):
	failed = False
	pg.init()
	if show == True:
		screen = pg.display.set_mode((755, 755))
		pg.display.set_caption("Snake")
	else:
		screen = 1
	snake = Snake()
	food = Food()
	score = 0
	timer = 0
	count = 1.0
	finalMove = 1
	while failed == False:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		if show == True:
			screen.fill((0,0,0))
		if count % counttime == 0:
			if 101 - count/counttime > 0:
				score += 1
			foodDirection = snake.getRelativeFoodPosition(food)
			adjObstacles = snake.getAdjObstacles()
			decision = nNetwork.evaluate([foodDirection[0], foodDirection[1], foodDirection[2], adjObstacles[0], adjObstacles[1], adjObstacles[2], adjObstacles[3], adjObstacles[4], adjObstacles[5], adjObstacles[6], adjObstacles[7], adjObstacles[8], adjObstacles[9], 1])
			if decision[0] >= decision[1] and decision[0] >= decision[2]:
				finalMove = snake.direction+1
			elif decision[1] >= decision[0] and decision[1] >= decision[2]:
				finalMove = snake.direction
			elif decision[2] >= decision[0] and decision[2] >= decision[1]:
				finalMove = snake.direction-1
			if finalMove == 0:
				finalMove = 4
			elif finalMove == 5:
				finalMove = 1
			snake.changeDirection(finalMove)
			if show == True:
				food.draw(screen)
			if snake.position == food.position:
				food.generate(snake.positions)
				snake.updateLength(screen, show)
				score += 150
				timer = 0
			else:
				snake.update(screen, False, show)
			if show == True:
				pg.display.flip()
			if snake.position[0] < 0 or snake.position[0] > 751 or snake.position[1] < 0 or snake.position[1] > 751:
				failed = True
			c = 0
			for pos in snake.positions:
				if snake.position == pos:
					if c >= 1:
						failed = True
					c += 1
		if timer >= counttime*150:
			failed = True
		count+=1
		timer+=1
	return score

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
	def updateLength(self, screen, show):
		self.length+=1
		if self.length == 900:
			boolean = True
		self.update(screen, True, show)
	def update(self, screen, new, show):
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
		if show == True:
			pg.draw.rect(screen, (255,255,255), (self.position[0], self.position[1], 20, 20))
			for pos in self.positions:
				pg.draw.rect(screen, (255,255,255), (pos[0], pos[1], 20, 20))
		self.positions.append(self.position)
	def getRelativeFoodPosition(self, food):
		rel = map(lambda x, y: y - x, self.position, food.position)
		relative = list(rel)
		angle = math.atan2(relative[-1], relative[0])
		if self.direction == 1:
			if abs(angle) == math.pi:
				return [0, 0, 0]
			elif angle > 0:
				return [0, 0, 1]
			elif angle < 0:
				return [1, 0, 0]
		elif self.direction == 2:
			if angle == (math.pi)/2:
				return [0, 0, 0]
			elif abs(angle) > (math.pi)/2:
				return [1, 0, 0]
			elif abs(angle) < (math.pi)/2:
				return [0, 0, 1]
		elif self.direction == 3:
			if abs(angle) == math.pi:
				return [0, 0, 0]
			elif angle > 0:
				return [1, 0, 0]
			elif angle < 0:
				return [0, 0, 1]
		elif self.direction == 4:
			if angle == -(math.pi)/2:
				return [0, 0, 0]
			elif abs(angle) > (math.pi)/2:
				return [0, 0, 1]
			elif abs(angle) < (math.pi)/2:
				return [1, 0, 0]
		return [0, 1, 0]
	def getAdjObstacles(self):
		absolute = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		relative = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for pos in self.positions:
			if self.position[0]+25 == pos[0] and self.position[1] == pos[1]:
				absolute[0] = 1
			if self.position[0]+25 == pos[0] and self.position[1]-25 == pos[1]:
				absolute[1] = 1
			if self.position[0] == pos[0] and self.position[1]-25 == pos[1]:
				absolute[2] = 1
			if self.position[0]-25 == pos[0] and self.position[1]-25 == pos[1]:
				absolute[3] = 1
			if self.position[0]-25 == pos[0] and self.position[1] == pos[1]:
				absolute[4] = 1
			if self.position[0]-25 == pos[0] and self.position[1]+25 == pos[1]:
				absolute[5] = 1
			if self.position[0] == pos[0] and self.position[1]+25 == pos[1]:
				absolute[6] = 1
			if self.position[0]+25 == pos[0] and self.position[1]+25 == pos[1]:
				absolute[7] = 1
			if self.position[0]+50 == pos[0] and self.position[1] == pos[1]:
				absolute[8] = 1
			if self.position[0] == pos[0] and self.position[1]-50 == pos[1]:
				absolute[9] = 1
			if self.position[0]-50 == pos[0] and self.position[1] == pos[1]:
				absolute[10] = 1
			if self.position[0] == pos[0] and self.position[1]+50 == pos[1]:
				absolute[11] = 1
		if self.position[0]+25 > 751:
			absolute[0] = 1
		if self.position[1]-25 < 0:
			absolute[2] = 1
		if self.position[0]-25 < 0:
			absolute[4] = 1
		if self.position[1]+25 > 751:
			absolute[6] = 1
		if self.position[0]+25 > 751 and self.position[1]-25 < 0:
			absolute[1] = 1
		if self.position[0]-25 < 0 and self.position[1]-25 < 0:
			absolute[3] = 1
		if self.position[0]-25 < 0 and self.position[1]+25 > 751:
			absolute[5] = 1
		if self.position[0]+25 > 751 and self.position[1]+25 > 751:
			absolute[7] = 1
		if self.position[0]+50 > 751:
			absolute[8] = 1
		if self.position[1]-50 < 0:
			absolute[9] = 1
		if self.position[0]-50 < 0:
			absolute[10] = 1
		if self.position[1]+50 > 751:
			absolute[11] = 1
		if self.direction == 1:
			relative[0] = absolute[3]
			relative[1] = absolute[2]
			relative[2] = absolute[1]
			relative[3] = absolute[0]
			relative[4] = absolute[7]
			relative[5] = absolute[6]
			relative[6] = absolute[5]
			relative[7] = absolute[9]
			relative[8] = absolute[8]
			relative[9] = absolute[11]
		elif self.direction == 2:
			relative[0] = absolute[5]
			relative[1] = absolute[4]
			relative[2] = absolute[3]
			relative[3] = absolute[2]
			relative[4] = absolute[1]
			relative[5] = absolute[0]
			relative[6] = absolute[7]
			relative[7] = absolute[10]
			relative[8] = absolute[9]
			relative[9] = absolute[8]
		elif self.direction == 3:
			relative[0] = absolute[7]
			relative[1] = absolute[6]
			relative[2] = absolute[5]
			relative[3] = absolute[4]
			relative[4] = absolute[3]
			relative[5] = absolute[2]
			relative[6] = absolute[1]
			relative[7] = absolute[11]
			relative[8] = absolute[10]
			relative[9] = absolute[9]
		elif self.direction == 4:
			relative[0] = absolute[1]
			relative[1] = absolute[0]
			relative[2] = absolute[7]
			relative[3] = absolute[6]
			relative[4] = absolute[5]
			relative[5] = absolute[4]
			relative[6] = absolute[3]
			relative[7] = absolute[8]
			relative[8] = absolute[11]
			relative[9] = absolute[10]
		return relative

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

class Neural_Network:
	def __init__(self, inputSize, outputSize, hiddenLayerCount, hiddenLayerSize, weights, mutateRate):
		self.inputSize = inputSize
		self.outputSize = outputSize
		self.hiddenLayerCount = hiddenLayerCount
		self.hiddenLayerSize = hiddenLayerSize
		self.weights = weights
		self.mutateRate = mutateRate
	def sigmoid(self, x):
		return (1/(1+math.exp(-x)))
	def evaluateNode(self, node, layer, inputs):
		count = 0
		value = 0
		for input in inputs:
			value+=input*self.weights[layer][node][count]
			count+=1
		return self.sigmoid(value)
	def evaluateLayer(self, layer, inputs):
		output = []
		for node in range(self.hiddenLayerSize):
			output.append(self.evaluateNode(node, layer, inputs))
		return output	
	def evaluate(self, inputs):
		finalInputs = inputs
		for layer in range(self.hiddenLayerCount):
			finalInputs = self.evaluateLayer(layer, finalInputs)
		output = []
		for node in range(self.outputSize):
			count = 0
			value = 0
			for input in finalInputs:
				value += input*self.weights[-1][node][count]
				count += 1
			output.append(self.sigmoid(value))
		return output
	def mutate(self):
		for layer in range(self.hiddenLayerCount):
			for node in range(self.hiddenLayerSize):
				for weight in range(len(self.weights[layer][node])):
					self.weights[layer][node][weight] += random.uniform(-1.0, 1.0)*self.mutateRate
		for node in range(self.outputSize):
			for weight in range(len(self.weights[-1][node])):
				self.weights[-1][node][weight] += random.uniform(-1.0, 1.0)*self.mutateRate
	def randomizeWeights(self):
		for layer in range(self.hiddenLayerCount):
			for node in range(self.hiddenLayerSize):
				for weight in range(len(self.weights[layer][node])):
					self.weights[layer][node][weight] = random.uniform(-1.0, 1.0)
		for node in range(self.outputSize):
			for weight in range(len(self.weights[-1][node])):
				self.weights[-1][node][weight] = random.uniform(-1.0, 1.0)

def main():
	failed = False
	snakes = {}
	for num in range(0, 100):
		snakes[Neural_Network(14,3,1,7,[[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]], .2)] = 0
	for snake in snakes:
			snake.randomizeWeights()
	for n in range(0, 1000):
		for snake in snakes:
			snakes[snake] = run_game(10.0, snake, False)
		sortedSnakes = sorted(snakes.items(), key=operator.itemgetter(1))
		print(n+1)
		print(sortedSnakes[-1][1])
		run_game(1000.0, sortedSnakes[-1][0], True)
		snakes = {}
		for num in range(0, 90):
			sortedSnakes.pop(0)
		for snake in snakes:
			del snakes[snake]
		for num in range(0, 90):
			newWeight = copy.deepcopy(sortedSnakes[num%10][0].weights)
			snakes[Neural_Network(6,3,1,4, newWeight, 1)] = 0
		for snake in snakes:
			snake.mutate()
		for num in range(0, 10):
			snakes[sortedSnakes[0][0]] = 0
			sortedSnakes.pop(0)

if __name__ == "__main__":	
	main()