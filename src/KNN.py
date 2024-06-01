import time
import numpy as np
import math
from data_loader import MNISTLoader
from distance_calculator import DistanceCalculator

class KNN:
    def __init__(self, train_images, test_image, train_labels, test_labels, distance_matrix, movement_matrix, k):

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
        self.distance_matrix = distance_matrix
        self.movement_matrix = movement_matrix
        self.k = k
        self.calculator = DistanceCalculator(distance_matrix, movement_matrix)
        
    def calculate_distances(self):
        """
        Laskee etäisyydet testikuvan ja harjoituskuvien välillä.

        Returns:
            Harjoituskuvien numeeriset arvot sekä etäisyydet testikuvaan.
        """

        test_image_points = [(i, j) for i in range(self.test_image.shape[0]) for j in range(self.test_image.shape[1]) if self.test_image[i, j] == 1]


        labels_and_distances = []

        for i, (train_image, train_label) in enumerate(zip(self.train_images, self.train_labels)):
            train_image_points = [(i, j) for i in range(train_image.shape[0]) for j in range(train_image.shape[1]) if train_image[i, j] == 1]

            distance_AB = self.calculator.distance_between_images(test_image_points, train_image_points, train_image)
            distance_BA = self.calculator.distance_between_images(train_image_points, test_image_points, self.test_image)
            total_distance = distance_AB + distance_BA

            labels_and_distances.append((train_label, total_distance))

        return labels_and_distances
    
    def predict(self):
        distances = self.calculate_distances()

        # Järjestetään etäisyydet pienimmästä suurimpaan
        distances.sort(key=lambda x: x[1])

        # Otetaan k lähintä naapuria
        k_nearest = distances[:self.k]

        # Haetaan näiden naapureiden labelit
        k_nearest_labels = [label for label, total_distance in k_nearest]

        return k_nearest_labels, self.test_labels