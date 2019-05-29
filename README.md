# Snake Evolution

This project is meant to demonstrate a simple AI learning program on the game Snake. The AI essentially learns through the natural selection and random mutation of neural networks on a population of 100 networks or snakes per generation. Visually, when run, the program first shows each snake of the first generation run through a game at an accelerated rate. It then shows the snake of that generation which performed the best, and repeats this process for the next generation. Behind the scenes, It takes the best performing snakes of each generation, scored on food eaten and time alive, and generates the new snake generation based on those.

#### Difficulties

The most difficult part of this program was getting all the parts of the neural network to function with variable input, output, hidden layer size, and hidden layer amount. It took a lot of breaking down and testing to see whether the network actually produced the correct values based on the inputs and to determine where exactly a bug was occuring when one did occur.
