import tkinter as tk
from tkinter import ttk, constants
import numpy as np
import time
import math
from data_loader import MNISTLoader
from KNN import KNN


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

        self.test_image_index = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=constants.BOTH, expand=True)

        # Testikuvien valinta
        ttk.Label(master=self._frame, text="Valitse testikuvana käytettävä numero:").pack(pady=10)
        
        self.buttons_frame = ttk.Frame(master=self._frame)
        self.buttons_frame.pack(pady=10)

        self.test_image_button_1 = ttk.Button(self.buttons_frame, text=f"{self.y_test[0]}", command=self.select_test_image_1)
        self.test_image_button_1.grid(row=0, column=0, padx=5)

        self.test_image_button_2 = ttk.Button(self.buttons_frame, text=f"{self.y_test[1]}", command=self.select_test_image_2)
        self.test_image_button_2.grid(row=0, column=1, padx=5)

        self.test_image_button_3 = ttk.Button(self.buttons_frame, text=f"{self.y_test[2]}", command=self.select_test_image_3)
        self.test_image_button_3.grid(row=0, column=2, padx=5)

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

    def select_test_image_1(self):
        self.test_image_index = 0
        self.test_image_button_1.config(style="Selected.TButton")
        self.test_image_button_2.config(style="TButton")
        self.test_image_button_3.config(style="TButton")

    def select_test_image_2(self):
        self.test_image_index = 1
        self.test_image_button_1.config(style="TButton")
        self.test_image_button_2.config(style="Selected.TButton")
        self.test_image_button_3.config(style="TButton")

    def select_test_image_3(self):
        self.test_image_index = 2
        self.test_image_button_1.config(style="TButton")
        self.test_image_button_2.config(style="TButton")
        self.test_image_button_3.config(style="Selected.TButton")

    def predict(self):

        try:
            if self.test_image_index is None:
                raise ValueError("Valitse testikuva ennen ennustamista.")
            test_image_index = self.test_image_index

            test_image = self.X_test[test_image_index]
            test_label = self.y_test[test_image_index]

            k = self.k_value.get()
            knn = KNN(self.X_train, test_image, self.y_train, test_label,  k=k)

            start_time = time.time()
            predicted_label, test_label = knn.predict()
            elapsed_time = time.time() - start_time

            # Näytä tulokset käyttöliittymässä
            self.result_label.config(text=f"Testikuva: {test_label}, Ennuste: {predicted_label}")
            self.time_label.config(text=f"Laskentaan käytetty aika: {elapsed_time:.4f} sekuntia")

        except ValueError as e:
            self.result_label.config(text=f"Virhe: {str(e)}")




