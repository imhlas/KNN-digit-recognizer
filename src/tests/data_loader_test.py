import unittest
import numpy as np
from sklearn.datasets import fetch_openml
from data_loader import DataLoader 

class TestMNISTLoader(unittest.TestCase):

    def setUp(self):
        self.loader = DataLoader(threshold_value=127)

    def test_load_data(self):
        data, target = self.loader.load_data()

        # Tarkistetaan datan muoto
        self.assertEqual(data.shape, (70000, 28, 28))
        self.assertEqual(target.shape, (70000,))

        # Tarkistaan binarisointi
        self.assertTrue(np.all((data == 0) | (data == 1)))
        self.assertTrue(np.issubdtype(target.dtype, np.integer))

    def test_split_data(self):

        self.loader.load_data()

        # Jaetaan data harjoitus- ja testidatoihin
        X_train, X_test, y_train, y_test = self.loader.split_data()

        # Tarkistetaan harjoitusdatan muoto
        self.assertEqual(X_train.shape, (60000, 28, 28))
        self.assertEqual(y_train.shape, (60000,))

        # Tarkistetaan testidatan muoto
        self.assertEqual(X_test.shape, (10000, 28, 28))
        self.assertEqual(y_test.shape, (10000,))

        # Tarkistetaa, että harjoitusdatan ja testidatan arvot ovat oikein
        self.assertTrue(np.array_equal(X_train, self.loader.data[:60000]))
        self.assertTrue(np.array_equal(X_test, self.loader.data[60000:]))
        self.assertTrue(np.array_equal(y_train, self.loader.target[:60000]))
        self.assertTrue(np.array_equal(y_test, self.loader.target[60000:]))
