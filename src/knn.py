"""
Moduuli, joka sisältää KNN-luokan
"""

import heapq
import time
import random
from distance_calculator import DistanceCalculator
from config import distances, moves

class KNN:
    """
    Luokka, joka edustaa K-lähimpien naapurien luokittelijaa.
    """
    def __init__(self, k, train_data, test_data, train_labels, test_labels,
                train_point_lists, test_point_lists, train_binary_matrices, test_binary_matrices):
        """
        Alustaa KNN-luokan.

        Args:
            k: Naapureiden lukumäärä KNN-algoritmille.
            train_data: Harjoitusaineiston kuvat.
            test_data: Testiaineiston kuvat.
            train_labels: Harjoitusaineiston numeeriset arvot.
            test_labels: Testiaineiston numeeriset arvot.
            train_point_lists: Lista harjoitusaineiston pisteistä.
            test_point_lists: Lista testiaineiston pisteistä.
            train_binary_matrices: Lista harjoitusaineiston binäärimatriiseista.
            test_binary_matrices: Lista testiaineiston binäärimatriiseista.
        """
        self.k = k
        self.train_data = train_data
        self.test_data = test_data
        self.train_labels = train_labels
        self.test_labels = test_labels
        self.train_point_lists = train_point_lists
        self.test_point_lists = test_point_lists
        self.train_binary_matrices = train_binary_matrices
        self.test_binary_matrices = test_binary_matrices
        self.calculator = DistanceCalculator(distances, moves)

    def calculate_distances(self, test_image_points, test_binary_matrix):
        """
        Laskee etäisyydet testikuvan ja harjoituskuvien välillä.

        Returns:
            Harjoituskuvien numeeriset arvot sekä etäisyydet testikuvaan.
        """
        k_nearest = []

        for i in range(len(self.train_data)):
            train_image_points = self.train_point_lists[i]
            train_label = self.train_labels[i]
            train_image_binary = self.train_binary_matrices[i]

            distance_ab = self.calculator.distance_between_images(test_image_points,
                                                                train_image_points,
                                                                train_image_binary)

            distance_ba = self.calculator.distance_between_images(train_image_points,
                                                                test_image_points,
                                                                test_binary_matrix)
            total_distance = distance_ab + distance_ba

            if len(k_nearest) < self.k:
                heapq.heappush(k_nearest, (-total_distance, train_label))
            else:
                heapq.heappushpop(k_nearest, (-total_distance, train_label))

        k_nearest = sorted([(-dist, label) for dist, label in k_nearest])
        return k_nearest

    def predict(self, test_image_points, test_binary_matrix):
        """
        Ennustaa testikuvan luokan perustuen lähimpiin naapureihin.

        Palauttaa:
            Tuplen, joka sisältää ennustetun arvon ja naapureiden luettelot.
        """

        calculated_distances = self.calculate_distances(test_image_points, test_binary_matrix)
        k_nearest_labels = [label for total_distance, label in calculated_distances]
        predicted_label = max(set(k_nearest_labels), key=k_nearest_labels.count)
        return predicted_label, k_nearest_labels

    def run(self, test_image_count):

        """
        Suorittaa KNN-algoritmin testikuvilla.

        Args:
            test_image_count: Testikuvien määrä

        Palauttaa:
            Tuplen, joka sisältää oikeiden ennusteiden määrän,
            virheellisten ennusteiden määrän, kokonaisajan, ennusteet ja testi-indeksit.
        """
        test_indices = random.sample(range(len(self.test_data)), test_image_count)

        x_test = self.test_data[test_indices]
        y_test = self.test_labels[test_indices]
        test_points = [self.test_point_lists[i] for i in test_indices]
        test_binary_matrices = [self.test_binary_matrices[i] for i in test_indices]

        correct_predictions = 0
        total_time = 0
        predictions = []

        for index in range(test_image_count):
            test_label = y_test[index]
            test_image_points = test_points[index]
            test_binary_matrix = test_binary_matrices[index]

            start_time = time.time()
            predicted_label, neighbors = self.predict(test_image_points, test_binary_matrix)
            elapsed_time = time.time() - start_time
            total_time += elapsed_time

            predictions.append((test_label, predicted_label, neighbors))

            if predicted_label == test_label:
                correct_predictions += 1

        incorrect_predictions = test_image_count - correct_predictions

        return correct_predictions, incorrect_predictions, total_time, predictions, test_indices
