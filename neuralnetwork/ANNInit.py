import numpy as np

def createWeights(layers):
    """
    Function takes as input a list numbers corresponding to the layers and returns weight matrices corresponding to that list
    """
    weights = [0]*(len(layers)-1)
    #create an empty list to fill with weights

    for i in range(len(weights)):
        #loop over the list of weights and set it to a np.array with the correct dimensions, uniformly distributed between -1 and 1
        dimension = (layers[i], layers[i+1])
        weights[i] = np.random.uniform(-1, 1., dimension)

    return weights

def createBiases(layers):
    """
    Function takes as input a list numbers corresponding to the layers and returns weight matrices corresponding to that list
    """
    biases = [0]*(len(layers)-1)
    #create an empty list to fill with weights

    for i in range(len(biases)):
        #loop over the list of weights and set it to a np.array with the correct dimensions, uniformly distributed between -1 and 1
        dimension = (layers[i+1])
        biases[i] = np.random.uniform(-1, 1., dimension)

    return biases
