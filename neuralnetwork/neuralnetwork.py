import numpy as np

class Dimensions:
    """ Structure for properties of neural network"""
    def __init__(self, inputNodes, layerAmounts, layerNodes, outputNodes):
        self.inputNodes = inputNodes
        self.layerAmounts = layerAmounts
        self.layerNodes = layerNodes
        self.outputNodes = outputNodes

class ArtificialNeuralNetwork:
    """ Neural network object"""
    def __init__(self, Dimensions, activationFunction):
        pass
