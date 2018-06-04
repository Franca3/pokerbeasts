from neuralnetwork import NNPlayer

class Population:
    """Population object"""

    def __init__(self,numOfMembers, dimensions, activationFunction):
        self.members = [0]*numOfMembers
        for i in range(numOfMembers):
            self.members[i] = NNPlayer(dimensions, activationFunction)

    def selection():
        pass

    def crossover():
        pass

    def mutation():
        #mutatie van 
        pass

    def generateNextGen():
        pass
