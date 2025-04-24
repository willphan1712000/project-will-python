import numpy as np

class Relu:
    '''
    Relu activation function
        @method activate: to get value passed over the function
    '''
    def activate(self, x):
        self.output = np.maximum(0, x)
        self.derivative = self.grad()

    def grad(self):
        return np.diag(np.where(self.output > 0, 1, 0).flatten())