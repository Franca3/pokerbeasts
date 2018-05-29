import numpy as np
import weightsInit
import feedForward

class ArtificialNeuralNetwork:
    """ Neural network object"""
    def __init__(self, dimensions, activationFunction):
        """
        dimensions is a list of numbers (eg. [7,3,3,2])
        activationfunctio is a string, either 'sigmoid' or 'linRect
        """
        self.weights = weightsInit.createWeights(dimensions)
        self.biases = weightsInit.createBiases(dimensions)
        self.activationFunction = activationFunction

    def generateOutput(self, inputLayer):
        """
        Method that returns an np.array of length 3, each corresponding to a move to make
        """
        return feedForward.feedForward(inputLayer, self.weights, self.biases, self.activationFunction)

    def generateMove(self, inputLayer):
        """
        Method that returns a move, either 'fold', 'call', 'raise'
        """

        moveDictionary = {0:"Fold", 1:"Call", 2:"Raise"}
        #create a move dictionary
        output = self.generateOutput(inputLayer)
        move = np.argmax(output)
        #take the index of the maximum value of the output
        return moveDictionary[move]

network = ArtificialNeuralNetwork([7,11,11,3],"sigmoid")
print(network.generateMove([1,0,1,0,1,0,1]))
