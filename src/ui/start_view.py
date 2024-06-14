import tkinter as tk
from tkinter import ttk, constants
import numpy as np
import time
import random
from data_loader import DataLoader
from ui.results_view import ResultsView
from knn import KNN


class StartView:
    def __init__(self, root):

        """
        Alustaa StartView-luokan.

        """

        self._root = root
        self._frame = None

        self.loader = DataLoader()
        self.data, self.target = self.loader.load_data()
        self.train_data, self.test_data, self.train_target, self.test_target = self.loader.split_data()

        self.test_image_count = tk.StringVar(value="5")
        self.train_image_count = tk.StringVar(value="10000")
        self.k_value = tk.StringVar(value="3")

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=constants.BOTH, expand=True)
        
        # Testikuvien määrän valinta
        ttk.Label(master=self._frame, text="Valitse testikuvien määrä (1-50):").pack(pady=10)
        test_image_count_entry = ttk.Entry(master=self._frame, textvariable=self.test_image_count)
        test_image_count_entry.pack(pady=10)

        # Harjoitusdatan määrän valinta
        ttk.Label(master=self._frame, text="Valitse harjoitusdatan määrä (1-60000):").pack(pady=10)
        train_image_count_entry = ttk.Entry(master=self._frame, textvariable=self.train_image_count)
        train_image_count_entry.pack(pady=10)


        # k-arvon valinta
        ttk.Label(master=self._frame, text="Valitse k-arvo:").pack(pady=10)
        k_entry = ttk.Entry(master=self._frame, textvariable=self.k_value)
        k_entry.pack(pady=10)

        # Ennusta-painike
        predict_button = ttk.Button(master=self._frame, text="Ennusta", command=self.predict)
        predict_button.pack(pady=10)

        # Tulosten näyttö
        self.result_label = ttk.Label(master=self._frame, text="")
        self.result_label.pack(pady=10)

    def predict(self):

        try:
            test_image_count_str = self.test_image_count.get()
            train_image_count_str = self.train_image_count.get()
            k_str = self.k_value.get()

            if not test_image_count_str.isdigit() or not train_image_count_str.isdigit() or not k_str.isdigit():
                raise ValueError("Kaikkien arvojen on oltava positiivisia kokonaislukuja.")
            
            test_image_count = int(test_image_count_str)
            train_image_count = int(train_image_count_str)
            k = int(k_str)
            

            if not (1 <= test_image_count <= 50):
                raise ValueError("Testikuvien määrän tulee olla välillä 1-50.")
            if not (1 <= train_image_count <= 60000):
                raise ValueError("Harjoitusdatan määrän tulee olla välillä 1-60000.")

            train_indices = random.sample(range(len(self.train_data)), train_image_count)
            test_indices = random.sample(range(len(self.test_data)), test_image_count)

            self.X_train = self.train_data[train_indices]
            self.y_train = self.train_target[train_indices]
            self.X_test = self.test_data[test_indices]
            self.y_test = self.test_target[test_indices]

            correct_predictions = 0
            total_time = 0
            predictions = []

            for index in range(test_image_count):
                test_image = self.X_test[index]
                test_label = self.y_test[index]

                knn = KNN(self.X_train, test_image, self.y_train, test_label, k=k)

                start_time = time.time()
                predicted_label, _ = knn.predict()
                elapsed_time = time.time() - start_time
                total_time += elapsed_time

                predictions.append((test_label, predicted_label))

                if predicted_label == test_label:
                    correct_predictions += 1

            incorrect_predictions = test_image_count - correct_predictions

            results_view = ResultsView(self._root, correct_predictions, incorrect_predictions, total_time, test_indices, predictions, self.retry)
            results_view.pack()
            self._frame.destroy()

        except ValueError as e:
            self.result_label.config(text=f"Virhe: {str(e)}")


    def retry(self):
        self._frame.destroy()
        start_view = StartView(self._root)
        start_view.pack()



