import numpy as np
from neuralnetwork import ANNInit
from neuralnetwork import feedForward

class ArtificialNeuralNetwork:
    """ Neural network object"""
    def __init__(self, dimensions, activationFunction):
        """
        dimensions is a list of numbers, giving the amount of nodes of each row (eg. [7,3,3,2])
        Activation function is function  given to each node
        """

        self.weights = ANNInit.createWeights(dimensions)
        self.biases = ANNInit.createBiases(dimensions)
        self.activationFunction = activationFunction

    def generateOutput(self, inputLayer):
        """
        Method that returns an np.array of length 3, each entry corresponding to a move
        """
        return feedForward.feedForward(inputLayer, self.weights, self.biases, self.activationFunction)

    def generateMove(self, inputLayer):
        """
        Method that returns a move, either 'fold', 'call', 'raise'
        """
        #create a move dictionary
        output = self.generateOutput(inputLayer)
        move = np.argmax(output)
        #take the index of the maximum value of the output
        #if the index is 0, fold, if the index is 1, call, if the index is 2, raise
        return move
