import numpy as np

def sigmoid(x):
    """code for a sigmoid function from R-->[0,1]"""
    return 1/(1+np.exp(-x))

def feedForward(inputLayer,weights,biases):
    """
    Takes an input layer and a list of weight matrices and a list of bias matrices as input and returns the output accoring to the matrix multiplication
    """
    for i in range(len(weights)):
        #loop over the weights, where each next layer is the dot product of the previous layer and the weight matrix
        inputLayer = np.dot(inputLayer,weights[i])
        inputLayer = inputLayer + biases[i]
        inputLayer = sigmoid(inputLayer)
    return inputLayer