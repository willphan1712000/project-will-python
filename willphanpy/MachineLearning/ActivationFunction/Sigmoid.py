import numpy as np

class Sigmoid:
    '''
    Sigmoid activation function
        @method activate: to get value passed over the function
    '''
    def __init__(self):
          pass
    
    def activate(x):
            return 1 / (1 + np.exp(-x))
    
