import tkinter as tk
from tkinter import ttk, constants
import numpy as np
import random
from PIL import Image, ImageTk
from data_loader import MNISTLoader
from distance_metrics import undirected_hausdorff, directed_hausdorff

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

        self.labels = []
        self.distances = []

        self._initialize()
        self._show_test_number_and_distances()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for i in range(len(self.X_train) + 1):
            label = ttk.Label(master=self._frame)
            label.grid(row=i, column=0, padx=10, pady=10)
            self.labels.append(label)

            distance = ttk.Label(master=self._frame)
            distance.grid(row=i, column=1, padx=10, pady=10)
            self.distances.append(distance)

    def _show_test_number_and_distances(self):

        single_image_matrix = self.X_test[0]
        single_image_label = self.y_test[0]

        print(single_image_matrix)

        single_image_points = [(i, j) for i in range(single_image_matrix.shape[0]) for j in range(single_image_matrix.shape[1]) if single_image_matrix[i, j] == 1]

        print(single_image_points)

        distances = []
        
        for train_image_vector in self.X_train:
            train_image_points = [(i, j) for i in range(train_image_vector.shape[0]) for j in range(train_image_vector.shape[1]) if train_image_vector[i, j] == 1]
            distances.append(directed_hausdorff(train_image_points, single_image_points, 'd6'))


        self.labels[0].config(text=f"Testinumero: {single_image_label}")

        for i in range(len(self.X_train)):
            self.labels[i + 1].config(text=self.y_train[i])
            self.distances[i + 1].config(text=f"Etäisyys: {distances[i]}")

        print(f"Vertailunumerot: {self.y_train}")

        print(f"Etäisyydet: {distances}")