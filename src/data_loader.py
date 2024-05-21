import numpy as np
from sklearn.datasets import fetch_openml

class MNISTLoader:
    def __init__(self, threshold_value=127):
        self.data = None
        self.target = None
        self.threshold_value = threshold_value
        
    def load_data(self):
        mnist = fetch_openml('mnist_784', version=1)
        self.data = mnist['data']
        self.target = mnist['target']


        return self.data, self.target