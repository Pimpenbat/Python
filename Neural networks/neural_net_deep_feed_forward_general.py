# Jack Barker

import numpy as np
from feed_forward_trainer import trainer

class NeuralNetwork(object):
    def __init__(self):
        #Define Hyperparameters
        self.inputLayerSize = 3
        self.hiddenLayerSize = 4
        self.outputLayerSize = 1

        #Weights (parameters)
        np.random.seed(1)
        self.synaptic_weight1 = np.random.random((self.inputLayerSize, self.hiddenLayerSize))
        self.synaptic_weight2 = np.random.random((self.hiddenLayerSize, self.hiddenLayerSize))
        self.synaptic_weight3 = np.random.random((self.hiddenLayerSize, self.outputLayerSize))

    def forward(self, x):
        #Propogate inputs though network
        self.layer2 = np.dot(x, self.synaptic_weight1)
        self.activation2 = self.sigmoid(self.layer2)
        #print(self.activation2)
        #print(self.synaptic_weight2)
        self.layer3 = np.dot(self.activation2, self.synaptic_weight2)
        self.activation3 = self.layer3
        #print(self.layer3)
        #print(self.activation3)
        self.layer4 = np.dot(self.activation3, self.synaptic_weight3)
        output = self.sigmoid(self.layer4)
        return output

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def errorFunction(self, x, y):
        #Compute error for given x,y, use weights already stored in class.
        self.output = self.forward(x)
        J = .5 * sum((y - self.output)**2)
        return J

    def errorFunction_derivative(self, x, y):
        self.output = self.forward(x)
        #Compute derivative with respect to synaptic_weight1, synaptic_weight2, and synaptic_weight3 for a given x and y.
        delta4 = np.multiply(-(y - self.output), self.sigmoid_derivative(self.sigmoid(self.layer4)))
        dJdW3 = np.dot(self.activation3.T, delta4)
        delta3 = np.multiply(delta4, self.sigmoid_derivative(self.sigmoid(self.layer3)))
        dJdW2 = np.dot(self.activation2.T, delta3)
        delta2 = np.dot(delta3, self.synaptic_weight2.T) * self.sigmoid_derivative(self.sigmoid(self.layer2))
        dJdW1 = np.dot(x.T, delta2)

        return dJdW1, dJdW2, dJdW3

    #Helper Functions:
    def getParams(self):
        #Get synaptic_weight1, synaptic_weight2, and synaptic_weight3 unrolled into vector:
        params = np.concatenate((self.synaptic_weight1.ravel(), self.synaptic_weight2.ravel(), self.synaptic_weight3.ravel()))
        return params

    def setParams(self, params):
        #Set synaptic_weight1, synaptic_weight2, and synaptic_weight3 using single paramater vector.
        W1_start = 0
        W1_end = self.hiddenLayerSize * self.inputLayerSize
        self.synaptic_weight1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize , self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize * self.hiddenLayerSize
        self.synaptic_weight2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.hiddenLayerSize))
        W3_end = W2_end + self.hiddenLayerSize * self.outputLayerSize
        self.synaptic_weight3 = np.reshape(params[W2_end:W3_end], (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, x, y):
        dJdW1, dJdW2, dJdW3 = self.errorFunction_derivative(x, future_value)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel(), dJdW3.ravel()))

def computeGradient(neural_network, x, y):
        params_0 = neural_network.getParams()
        numgrad = np.zeros(params_0.shape)
        perturb = np.zeros(params_0.shape)
        e = 1e-4

        for p in range(len(params_0)):
            #Set perturbation vector
            perturb[p] = e
            neural_network.setParams(params_0 + perturb)
            loss2 = neural_network.errorFunction(x, future_value)

            neural_network.setParams(params_0 - perturb)
            loss1 = neural_network.errorFunction(x, future_value)

            #Compute Gradient
            numgrad[p] = (loss2 - loss1) / (2 * e)

            #Return the value we changed to zero:
            perturb[p] = 0

        #Return Params to original value:
        neural_network.setParams(params_0)

        return numgrad

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    print('Random synaptic weights1: ')
    print(neural_network.synaptic_weight1)
    print('Random synaptic weights2: ')
    print(neural_network.synaptic_weight2)
    print('Random synaptic weights3: ')
    print(neural_network.synaptic_weight3)

    #better data will find
    conditions = np.array(([[2, 4, 1], [8, 2, 0], [10, 2, 9]]), dtype = float)

    future_value = np.array(([45], [34], [93]), dtype = float)

    #Normalize
    future_value = future_value / 100

    T = trainer(neural_network)
    T.train(conditions, future_value)

    print('Trained synaptic_weights1: ')
    print(neural_network.synaptic_weight1)
    print('Trained synaptic_weights2: ')
    print(neural_network.synaptic_weight2)

    print('Output: ')
    print(neural_network.forward(conditions))
