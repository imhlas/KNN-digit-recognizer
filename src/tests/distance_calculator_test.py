import unittest
import numpy as np
from config import distances, moves
from distance_calculator import DistanceCalculator

class TestDistanceCalculator(unittest.TestCase):

    def setUp(self):
        """
        Alustaa DistanceCalculator-luokan testejä varten tarvittavat muuttujat.
        """
        self.calculator = DistanceCalculator(distances, moves)
    
    def test_calculate_distance(self):
        """
        Testaa etäisyyden laskemisen kahden pisteen välillä.
        Käyttää pisteitä (0, 0) ja (3, 4), joiden välinen etäisyys pitäisi olla 25.
        """
        point1 = (0, 0)
        point2 = (3, 4)
        distance = self.calculator.calculate_distance(point1, point2)
        self.assertEqual(distance, 25)
    
    def test_distance_between_images(self):
        """
        Testaa etäisyyden laskeminen kahden kuvan välillä.
        """

        image_a_points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        image_b_points = [(1, 1), (2, 2), (3, 3), (4, 4)]
        image_b_matrix = np.zeros((28, 28))
        for point in image_b_points:
            image_b_matrix[point] = 1

        distance = self.calculator.distance_between_images(image_a_points, image_b_points, image_b_matrix)
        self.assertEqual(distance, 2)

    def test_no_match_found(self):
        """
        Testaa tilannetta, jossa yhtään pistettä ei löydy läheltä ja käytetään calculate_distance-funktiota.
        """
  
        image_a_points = [(0, 0), (1, 1)]
        image_b_points = [(10, 10), (15, 15)]
        image_b_matrix = np.zeros((28, 28))
        for point in image_b_points:
            image_b_matrix[point] = 1
        
        # Lasketaan odotettu etäisyys käsin
        expected_distance = sum([min([self.calculator.calculate_distance(a, b) for b in image_b_points]) for a in image_a_points])

        distance = self.calculator.distance_between_images(image_a_points, image_b_points, image_b_matrix)
        self.assertEqual(distance, expected_distance)