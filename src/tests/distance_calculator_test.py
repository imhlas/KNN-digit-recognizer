"""
Moduuli, joka sisältää testit DistanceCalculator-luokalle.
"""

import unittest
import numpy as np
from config import distances, moves
from distance_calculator import DistanceCalculator

class TestDistanceCalculator(unittest.TestCase):
    """
    Luokka, joka testaa DistanceCalculator-luokkaa.
    """

    def setUp(self):
        """
        Alustaa DistanceCalculator-luokan testejä varten tarvittavat muuttujat.
        """
        self.calculator = DistanceCalculator(distances, moves)


    def test_distance_between_images(self):
        """
        Testaa etäisyyden laskeminen kahden kuvan välillä.
        """

        image_a_points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        image_b_points = [(1, 1), (2, 2), (3, 3), (4, 4)]
        image_b_matrix = np.zeros((28, 28))
        for point in image_b_points:
            image_b_matrix[point] = 1

        distance = self.calculator.distance_between_images(
                    image_a_points, image_b_points, image_b_matrix)

        self.assertEqual(distance, 2)

    def test_no_match_found(self):
        """
        Testaa tilannetta, jossa yhtään pistettä ei löydy
        läheltä ja käytetään calculate_distance-funktiota.
        """

        image_a_points = [(0, 0), (1, 1)]
        image_b_points = [(10, 10), (15, 15)]
        image_b_matrix = np.zeros((28, 28))
        for point in image_b_points:
            image_b_matrix[point] = 1

        # Lasketaan odotettu etäisyys käsin
        expected_distance = sum([min([(a[0] - b[0]) ** 2 +
                                      (a[1] - b[1]) ** 2 for b in image_b_points])
                                      for a in image_a_points])

        distance = self.calculator.distance_between_images(
                    image_a_points, image_b_points, image_b_matrix)

        self.assertEqual(distance, expected_distance)
