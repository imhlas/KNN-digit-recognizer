"""
Moduuli, joka lataa MNIST-datan OpenML-palvelusta ja prosessoi sen.
"""

import numpy as np
from sklearn.datasets import fetch_openml

class DataLoader:
    """
    Luokka, joka lataa MNIST-datan OpenML-palvelusta ja prosessoi sen.
    """

    def __init__(self, threshold_value=127):
        """
        Alustaa DataLoader-luokan.

        Args:
        threshold_value: Arvo, jonka perusteella kuvat binarisoidaan. Oletusarvo on 127.
        """

        self.data = None
        self.target = None
        self.threshold_value = threshold_value
        self.binary_matrices = None

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
        self.point_lists = [self.calculate_points(image) for image in self.data]
        self.binary_matrices = [(image == 1) for image in self.data]

    def calculate_points(self, image):
        """
        Laskee kuvapisteet binarisoidusta kuvasta.

        Args:
        image: Binarisoitu kuva (28x28).

        Returns:
        points: Lista pisteistä, joissa kuvassa on 1.
        """
        points = [(i, j) for i in range(image.shape[0])
                    for j in range(image.shape[1]) if image[i][j] == 1]

        return points

    def split_data(self, train_size):
        """
        Jakaa datan harjoitus- ja testidatoihin käyttäjän valitseman harjoitusdatan määrän mukaan.

        Args:
        train_size: Käyttäjän valitsema harjoitusdatan määrä (10000, 30000 tai 60000).

        Returns:
        (X_train, X_test, y_train, y_test):
        X_train ja y_train ovat harjoitusdatan kuvat ja etiketit,
        ja X_test ja y_test ovat testidatan kuvat ja etiketit.

        """
        x_train = self.data[:train_size]
        y_train = self.target[:train_size].to_numpy()
        point_lists_train = self.point_lists[:train_size]
        binary_matrices_train = self.binary_matrices[:train_size]

        x_test = self.data[60000:]
        y_test = self.target[60000:].to_numpy()
        point_lists_test = self.point_lists[60000:]
        binary_matrices_test = self.binary_matrices[60000:]

        return (x_train, x_test, y_train, y_test, point_lists_train, point_lists_test,
                binary_matrices_train, binary_matrices_test)
    