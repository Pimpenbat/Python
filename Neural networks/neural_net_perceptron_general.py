import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = np.random.random((3, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        #Given the small task, the brute force method gets the job done.
        for i in range(training_iterations):
            outputs = self.think(training_inputs)

            error = training_outputs - outputs
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(self.sigmoid(outputs)))
            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        outputs = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return outputs

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    print('Random synaptic weights: ')
    print(neural_network.synaptic_weights)

    training_inputs = np.array([[0,0,1],
                               [1,1,1],
                               [1,0,1],
                               [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 10000)

    print('Synaptic weights after training: ')
    print(neural_network.synaptic_weights)

    A = str(input("Entry 1: "))
    B = str(input("Entry 2: "))
    C = str(input("Entry 3: "))

    print('Perceptron function: input data = ', A, B, C)
    print('Output data: ')
    print(neural_network.think(np.array([A, B, C])))
