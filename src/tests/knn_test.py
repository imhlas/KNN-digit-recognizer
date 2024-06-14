import unittest
import numpy as np
from KNN import KNN

class TestKNN(unittest.TestCase):

    def setUp(self):
        """
        Alustaa testit.
        """
        
        # Luodaan täynnä nollia olevat 28x28 matriisit harjoitus- ja testikuville
        self.train_images = np.zeros((2, 28, 28), dtype=int)
        self.test_image = np.zeros((28, 28), dtype=int)

        # Asetetaan pisteitä harjoituskuvaan 1
        self.train_images[0][0][1] = 1
        self.train_images[0][1][0] = 1
        self.train_images[0][2][0] = 1

        # Asetetaan pisteitä harjoituskuvaan 2
        self.train_images[1][0][1] = 1
        self.train_images[1][1][0] = 1
        self.train_images[1][2][2] = 1

        # Asetetaan pisteitä testikuvaan
        self.test_image[0][1] = 1
        self.test_image[1][0] = 1
        self.test_image[2][2] = 1

        # Määritetään harjoitus- ja testikuvien labelit
        self.train_labels = np.array([0, 1])
        self.test_labels = np.array([1])
        self.k = 1
        self.knn = KNN(self.train_images, self.test_image, self.train_labels, self.test_labels, self.k)

    def test_calculate_distances(self):
        """
        Testaa etäisyyksien laskeminen testikuvan ja harjoituskuvien välillä.
        """
        k_nearest = self.knn.calculate_distances()
        self.assertEqual(len(k_nearest), self.k)
        self.assertEqual(k_nearest[0][1], 1)  

    def test_predict(self):
        """
        Testaa ennusteen laskeminen.
        """
        predicted_label, test_labels = self.knn.predict()
        self.assertEqual(predicted_label, 1)
        self.assertEqual(test_labels[0], self.test_labels[0])