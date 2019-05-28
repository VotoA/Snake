import sys
import random
import math

def main():
	NN = Neural_Network(6,3,1,4,[[[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]],[[1.0, 1.0, 1.0, 1.0, 1.0],[1.0, 1.0, 1.0, 1.0, 1.0],[1.0, 1.0, 1.0, 1.0, 1.0]]], 1)
	print(NN.evaluate([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]))
	NN.mutate()
	print(NN.evaluate([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]))

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


if __name__ == "__main__":	
	main()