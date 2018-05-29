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

    def generateOuput(self, inputLayer):

        return feedForward.feedForward(inputLayer, self.weights, self.biases, self.activationFunction)

network = ArtificialNeuralNetwork([7,11,11,3],"sigmoid")
print(network.generateOuput([0,1,0,1,0,1,0]))
