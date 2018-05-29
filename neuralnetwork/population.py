import numpy as np
from neuralnetwork import ArtificialNeuralNetwork

class Population:
    """Population object"""

    def __init__(self,numOfMembers, dimensions, activationFunction):
        self.members = [0]*numOfMembers
        for i in range(numOfMembers):
            self.members[i] = ArtificialNeuralNetwork(dimensions, activationFunction)

    def selection:
        pass

    def crossover():
        pass

    def mutation():
        pass

    def generateNextGen():
        pass
