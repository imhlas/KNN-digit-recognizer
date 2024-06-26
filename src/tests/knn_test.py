"""
Tiedosto, joka sisältää testit KNN-luokalle.
"""

import unittest
import numpy as np
from knn import KNN

class TestKNN(unittest.TestCase):
    """
    Luokka, joka testaa KNN-luokkaa.
    """

    def setUp(self):
        """
        Alustaa testit.
        """

        # Luodaan täynnä nollia olevat 28x28 matriisit harjoitus- ja testikuville
        self.train_images = np.zeros((2, 28, 28), dtype=int)
        self.test_images = np.zeros((2, 28, 28), dtype=int)

        # Asetetaan pisteitä harjoituskuvaan 1
        self.train_images[0][0][1] = 1
        self.train_images[0][1][0] = 1
        self.train_images[0][2][0] = 1

        # Asetetaan pisteitä harjoituskuvaan 2
        self.train_images[1][0][1] = 1
        self.train_images[1][1][0] = 1
        self.train_images[1][2][2] = 1

        # Asetetaan pisteitä testikuviin
        self.test_images[0][0][1] = 1
        self.test_images[0][1][0] = 1
        self.test_images[0][2][0] = 1

        self.test_images[1][0][1] = 1
        self.test_images[1][1][0] = 1
        self.test_images[1][2][2] = 1

        # Määritetään harjoitus- ja testikuvien labelit
        self.train_labels = np.array([0, 1])
        self.test_labels = np.array([0, 1])
        self.k = 1

        # Lisätään point_lists ja binary_matrices
        self.train_point_lists = [[(0, 1), (1, 0), (2, 0)], [(0, 1), (1, 0), (2, 2)]]
        self.test_point_lists = [[(0, 1), (1, 0), (2, 0)], [(0, 1), (1, 0), (2, 2)]]

        self.train_binary_matrices = [(self.train_images[0] == 1), (self.train_images[1] == 1)]
        self.test_binary_matrices = [(self.test_images[0] == 1), (self.test_images[1] == 1)]

        self.knn = KNN(
            self.k,
            self.train_images,
            self.test_images,
            self.train_labels,
            self.test_labels,
            self.train_point_lists,
            self.test_point_lists,
            self.train_binary_matrices,
            self.test_binary_matrices
        )

    def test_calculate_distances(self):
        """
        Testaa etäisyyksien laskeminen testikuvan ja harjoituskuvien välillä.
        """
        k_nearest = self.knn.calculate_distances(self.test_point_lists[0],
                                                self.test_binary_matrices[0])

        self.assertEqual(len(k_nearest), self.k)
        self.assertEqual(k_nearest[0][1], 0)

    def test_predict(self):
        """
        Testaa ennusteen laskeminen.
        """
        predicted_label, test_labels = self.knn.predict(self.test_point_lists[0],
                                                        self.test_binary_matrices[0])
        self.assertEqual(predicted_label, 0)
        self.assertEqual(test_labels[0], self.test_labels[0])

    def test_run(self):
        """
        Testaa run-metodi.
        """
        (correct_predictions, incorrect_predictions,
         total_time, predictions,test_indices) = self.knn.run(2)

        # Tarkistetaan ennustusten määrä
        self.assertEqual(correct_predictions, 2)
        self.assertEqual(incorrect_predictions, 0)

        # Tarkistetaan, että jokaisella ennusteella on oikeat arvot
        for i, (true_label, predicted_label, neighbors) in enumerate(predictions):
            self.assertEqual(true_label, self.test_labels[test_indices[i]])
            self.assertEqual(predicted_label, self.test_labels[test_indices[i]])
            self.assertEqual(len(neighbors), self.k)
