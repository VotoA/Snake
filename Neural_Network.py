import sys
import math

def main():
	NN = Neural_Network(2,1,1,2,[[[1.0, 1.0, 1.0],[1.0, 1.0, 1.0]],[[1.0, 1.0, 1.0]]])
	print(NN.evaluate([1.0, 0.0]))
	

class Neural_Network:
	def __init__(self, inputSize, outputSize, hiddenLayerCount, hiddenLayerSize, weights):
		self.inputSize = inputSize
		self.outputSize = outputSize
		self.hiddenLayerCount = hiddenLayerCount
		self.hiddenLayerSize = hiddenLayerSize
		self.weights = weights
	def sigmoid(self, x):
		return (1/(1+math.exp(-x)))
	def evaluateNode(self, node, layer, inputs):
		count = 0
		value = 0
		for input in inputs:
			value+=input*self.weights[layer][node][count]
			count+=1
		value+=1*self.weights[layer][node][count]
		print(self.sigmoid(value))
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
		for node in range(self.outputSize):
			value = self.evaluateNode(node, -1, finalInputs)
		return value

if __name__ == "__main__":	
	main()