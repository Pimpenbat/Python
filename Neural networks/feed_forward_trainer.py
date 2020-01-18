from scipy import optimize

class trainer(object):
    def __init__(self, neural_network):
        #Make Local reference to network:
        self.neural_network = neural_network

    def callbackF(self, params):
        self.neural_network.setParams(params)
        self.J.append(self.neural_network.errorFunction(self.x, self.y))

    def errorFunctionWrapper(self, params, x, y):
        self.neural_network.setParams(params)
        error = self.neural_network.errorFunction(x, y)
        grad = self.neural_network.computeGradients(x, y)
        return error, grad

    def train(self, x, y):
        #Make an internal variable for the callback function:
        self.x = x
        self.y = y

        #Make empty list to store error values:
        self.J = []

        params0 = self.neural_network.getParams()

        options = {'maxiter': 200, 'disp' : True}
        res = optimize.minimize(self.errorFunctionWrapper, params0, jac=True, method='BFGS',
                                 args=(x, y), options=options, callback=self.callbackF)

        self.neural_network.setParams(res.x)
        self.optimizationResults = res
