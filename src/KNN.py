import heapq
import numpy as np
from distance_calculator import DistanceCalculator
from config import distances, moves

class KNN:
    def __init__(self, train_images, test_image, train_labels, test_labels, k):

        """
        Alustaa KNN-luokan.

        Args:
            train_images: Harjoitusaineiston kuvat.
            test_images: Testiaineiston kuvat.
            train_labels: Harjoitusaineiston numeeriset arvot.
            test_labels: Testiaineiston numeeriset arvot.
            distance_matrix: Matriisi etäisyyksistä.
            movement_matrix: Lista mahdollisista liikkeistä koordinaatistossa.
            k: Naapureiden lukumäärä KNN-algoritmille.
        """
        self.train_images = train_images
        self.test_image = test_image
        self.train_labels = train_labels
        self.test_labels = test_labels
        self.k = k
        self.calculator = DistanceCalculator(distances, moves)
        
    def calculate_distances(self):
        """
        Laskee etäisyydet testikuvan ja harjoituskuvien välillä.

        Returns:
            Harjoituskuvien numeeriset arvot sekä etäisyydet testikuvaan.
        """

        test_image_points = [(i, j) for i in range(self.test_image.shape[0]) for j in range(self.test_image.shape[1]) if self.test_image[i, j] == 1]


        k_nearest = []

        for i, (train_image, train_label) in enumerate(zip(self.train_images, self.train_labels)):
            train_image_points = [(i, j) for i in range(train_image.shape[0]) for j in range(train_image.shape[1]) if train_image[i, j] == 1]

            distance_AB = self.calculator.distance_between_images(test_image_points, train_image_points, train_image)
            distance_BA = self.calculator.distance_between_images(train_image_points, test_image_points, self.test_image)
            total_distance = distance_AB + distance_BA

            # Jos keossa on vähemmän kuin k alkiota, lisätään uusi alkio
            if len(k_nearest) < self.k:
                heapq.heappush(k_nearest, (-total_distance, train_label))
            else:
                # Jos keossa on jo k alkiota, lisätään uusi alkio vain jos se on pienempi kuin keon maksimi
                heapq.heappushpop(k_nearest, (-total_distance, train_label))

        # Muutetaan keko listaksi ja järjestetään se pienimmästä suurimpaan etäisyyteen
        k_nearest = sorted([(-dist, label) for dist, label in k_nearest])

        return k_nearest
    
    def predict(self):
        distances = self.calculate_distances()

        k_nearest_labels = [label for total_distance, label in distances]

        return k_nearest_labels, self.test_labels