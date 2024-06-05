import tkinter as tk
from tkinter import ttk, constants
import numpy as np
import time
import math
from data_loader import MNISTLoader
from KNN import KNN

distances = [[18, 13, 10, 9, 10, 13, 18],
             [13, 8, 5, 4, 5, 8, 13],
             [10, 5, 2, 1, 2, 5, 10],
             [9, 4, 1, 0, 1, 4, 9],
             [10, 5, 2, 1, 2, 5, 10],
             [13, 8, 5, 4, 5, 8, 13],
            [18, 13, 10, 9, 10, 13, 18]]

moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 2),
       (0, -2), (2, 0), (-2, 0), (-1, 2), (2, 1), (-1, -2), (1, -2), (-2, 1), (-2, -1),
       (1, 2), (2, -1), (-2, -2), (-2, 2), (2, -2), (2, 2), (0, 3), (0, -3),
       (3, 0), (-3, 0), (1, 3), (-3, -1), (1, -3), (3, 1), (-1, 3), (-1, -3),
       (-3, 1), (3, -1), (-3, 2), (3, 2), (2, -3), (-2, -3), (3, -2), (-3, -2),
       (2, 3), (-2, 3), (-3, -3), (-3, 3), (3, -3), (3, 3)]

class StartView:
    def __init__(self, root):

        """
        Alustaa StartView-luokan.

        """

        self._root = root
        self._frame = None

        self.loader = MNISTLoader()
        self.data, self.target = self.loader.load_data()
        self.X_train, self.X_test, self.y_train, self.y_test = self.loader.split_data()

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=constants.BOTH, expand=True)

        # Testinumeron labeli
        ttk.Label(master=self._frame, text=f"Testinumeron labeli: {self.y_test[0]}").pack(pady=10)

        # k-arvon valinta
        ttk.Label(master=self._frame, text="Valitse k-arvo:").pack(pady=10)
        self.k_value = tk.IntVar(value=3)
        k_entry = ttk.Entry(master=self._frame, textvariable=self.k_value)
        k_entry.pack(pady=10)

        # Ennusta-painike
        predict_button = ttk.Button(master=self._frame, text="Ennusta", command=self.predict)
        predict_button.pack(pady=10)

        # Tulosten näyttö
        self.result_label = ttk.Label(master=self._frame, text="")
        self.result_label.pack(pady=10)

        self.time_label = ttk.Label(master=self._frame, text="")
        self.time_label.pack(pady=10)

    def predict(self):
        k = self.k_value.get()
        knn = KNN(self.X_train, self.X_test[0], self.y_train, self.y_test[0], distances, moves, k=k)

        start_time = time.time()
        predicted_label, test_label = knn.predict()
        elapsed_time = time.time() - start_time

        # Näytä tulokset käyttöliittymässä
        self.result_label.config(text=f"Ennustettu label: {predicted_label}")
        self.time_label.config(text=f"Laskentaan käytetty aika: {elapsed_time:.4f} sekuntia")




