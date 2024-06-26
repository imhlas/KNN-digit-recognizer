"""
Moduuli, joka sisältää testit DataLoader-luokalle.
"""

import unittest
import numpy as np
from data_loader import DataLoader

class TestMNISTLoader(unittest.TestCase):
    """
    Luokka, joka testaa DataLoader-luokkaa.
    """

    def setUp(self):
        """
        Alustaa testit.
        """
        self.loader = DataLoader(threshold_value=127)

    def test_load_data(self):
        """
        Testaa datan lataamista.
        """
        self.loader.load_data()
        data, target = self.loader.data, self.loader.target

        # Tarkistetaan datan muoto
        self.assertEqual(data.shape, (70000, 28, 28))
        self.assertEqual(target.shape, (70000,))

        # Tarkistaan binarisointi
        self.assertTrue(np.all((data == 0) | (data == 1)))
        self.assertTrue(np.issubdtype(target.dtype, np.integer))

    def test_split_data(self):
        """
        Testaa datan jakamista harjoitus- ja testidataan.
        """

        self.loader.load_data()

        # Jaetaan data harjoitus- ja testidatoihin
        (x_train, x_test, y_train, y_test, train_point_lists, test_point_lists,
         train_binary_matrices, test_binary_matrices) = self.loader.split_data(60000)

        # Tarkistetaan harjoitusdatan muoto
        self.assertEqual(x_train.shape, (60000, 28, 28))
        self.assertEqual(y_train.shape, (60000,))

        # Tarkistetaan testidatan muoto
        self.assertEqual(x_test.shape, (10000, 28, 28))
        self.assertEqual(y_test.shape, (10000,))

        # Tarkistetaan pistelista ja matriisi
        self.assertEqual(len(train_point_lists), 60000)
        self.assertEqual(len(test_point_lists), 10000)
        self.assertEqual(len(train_binary_matrices), 60000)
        self.assertEqual(len(test_binary_matrices), 10000)

        # Tarkistetaa, että harjoitusdatan ja testidatan arvot ovat oikein
        self.assertTrue(np.array_equal(x_train, self.loader.data[:60000]))
        self.assertTrue(np.array_equal(x_test, self.loader.data[60000:]))
        self.assertTrue(np.array_equal(y_train, self.loader.target[:60000]))
        self.assertTrue(np.array_equal(y_test, self.loader.target[60000:]))
