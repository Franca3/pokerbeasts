import numpy as np

import weightsInit

class ArtificialNeuralNetwork:
    """ Neural network object"""
    def __init__(self, dimensions, activationFunction):
        self.weights = weightsInit.createWeights(dimensions)
        self.biases = weightsInit.createBiases(dimensions)

network = ArtificialNeuralNetwork([7,11,11,3],None)
