import numpy as np
from sklearn.datasets import fetch_openml

class MNISTLoader:
    def __init__(self, threshold_value=127):
        self.data = None
        self.target = None
        self.threshold_value = threshold_value
        
    def load_data(self):
        mnist = fetch_openml('mnist_784', version=1)

        self.data = mnist['data'].reshape(-1, 28, 28)
        self.target = mnist['target'].astype(np.uint8)

        self.data = (self.data > self.threshold_value).astype(np.uint8)

        return self.data, self.target
    
    def split_data(self):
        X_train = self.data[10:20]
        X_test = self.data[60000:60010]
        y_train = self.target[10:20]
        y_test = self.target[60000:60010]

        return X_train, X_test, y_train, y_test
    
