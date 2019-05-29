# Snake Evolution

This project is meant to demonstrate a simple AI learning program on the game Snake. The AI essentially learns through the natural selection and random mutation of neural networks on a population of 100 networks or snakes per generation. Visually, when run, the program first shows each snake of the first generation run through a game at an accelerated rate. It then shows the snake of that generation which performed the best, and repeats this process for the next generation. Behind the scenes, It takes the best performing snakes of each generation, scored on food eaten and time alive, and generates the new snake generation based on those.

#### Difficulties

The most difficult part of this program was getting all the parts of the neural network to function with variable input, output, hidden layer size, and hidden layer amount. It took a lot of breaking down and testing to see whether the network actually produced the correct values based on the inputs and to determine where exactly a bug was occuring when one did occur.

```Python
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
```
The Code above is the aforementioned polymorphic neural network. It's main function can be seen in the evaluate function which takes inputs from another program and calculates a decision based on certain weights and the sigmoid equation. It also has secondary functions in the mutate and randomizeWeights functions. These are meant to change the weights of the network either completely or based on a previous weight set.

### Author
* **Anthony Voto**

### Acknoledgments
* My Brothers
* Various Stack Overflow users
* Code Bullet
