import numpy as np
from sklearn.datasets import fetch_openml

class MNISTLoader:
    def __init__(self, threshold_value=127):
        """
        Alustaa MNISTLoader-luokan.

        Args:
        threshold_value: Arvo, jonka perusteella kuvat binarisoidaan. Oletusarvo on 127.
        """

        self.data = None
        self.target = None
        self.threshold_value = threshold_value
        
    def load_data(self):
        """
        Lataa MNIST-datan OpenML-palvelusta ja prosessoi sen.

        Datan lataamisen jälkeen kuvat binarisoidaan käyttäen asetettua threshold-arvoa.

        Returns:
        (data, target): data on binarisoituja kuvia ja target vastaavia numeroarvoja.
        """

        mnist = fetch_openml('mnist_784', version=1)

        self.data = mnist['data'].to_numpy().reshape(-1, 28, 28)
        self.target = mnist['target'].astype(np.uint8)

        self.data = (self.data > self.threshold_value).astype(np.uint8)

        return self.data, self.target
    
    def split_data(self):
        """
        Jakaa datan harjoitus- ja testidatoihin.

        Returns:
        (X_train, X_test, y_train, y_test): X_train ja y_train ovat harjoitusdatan kuvat ja etiketit,
                                            ja X_test ja y_test ovat testidatan kuvat ja etiketit.

        """
        X_train = self.data[:10000]
        X_test = self.data[60000:60003]
        y_train = self.target[:10000].to_numpy()
        y_test = self.target[60000:60003].to_numpy()

        return X_train, X_test, y_train, y_test
    
