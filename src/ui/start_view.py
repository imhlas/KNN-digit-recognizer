"""
Moduuli, joka sisältää StartView-luokan.
"""

import tkinter as tk
from tkinter import ttk, constants
from data_loader import DataLoader
from knn import KNN
from ui.results_view import ResultsView

class StartView:
    """
    Luokka, joka esittää aloitusnäkymän käyttäjälle.
    """

    def __init__(self, root):
        """
        Alustaa StartView-luokan.
        """
        self._root = root
        self._frame = None

        self.loader = None
        self.train_data = None
        self.test_data = None
        self.train_target = None
        self.test_target = None
        self.train_point_lists = None
        self.test_point_lists = None
        self.train_binary_matrices = None
        self.test_binary_matrices = None

        self.test_image_count = tk.StringVar(value="5")
        self.train_image_count = tk.StringVar(value="10000")
        self.k_value = tk.StringVar(value="3")
        self.result_label = None

        self.initialize()

    def pack(self):
        """
        Pakkaa aloitusnäkymän.
        """
        self._frame.pack(fill=constants.BOTH, expand=True)

    def initialize(self):
        """
        Luo käyttöliittymäkomponentit StartView-luokkaan.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=constants.BOTH, expand=True)

        # Harjoitusdatan määrän valinta
        ttk.Label(
            master=self._frame,
            text="Valitse mallin kouluttamiseen käytettävien harjoituskuvien määrä:").pack(pady=10)

        train_10000_button =ttk.Button(
                            master=self._frame,text="10 000 kpl",
                            command=lambda: self.set_train_image_count(10000))

        train_10000_button.pack(pady=10)

        train_30000_button =ttk.Button(
                            master=self._frame, text="30 000 kpl",
                            command=lambda: self.set_train_image_count(30000))

        train_30000_button.pack(pady=10)

        train_60000_button =ttk.Button(
                            master=self._frame, text="60 000 kpl",
                            command=lambda: self.set_train_image_count(60000))

        train_60000_button.pack(pady=10)

        self.loading_label = ttk.Label(master=self._frame, text="")
        self.loading_label.pack(pady=10)

    def set_train_image_count(self, count):
        """
        Asettaa koulutusdatan määrän ja aloittaa datan lataamisen.

        Args:
            count: Koulutusdatan kuvien määrä.
        """
        self.train_image_count.set(str(count))
        self.show_loading_message()
        self.load_data(count)

    def show_loading_message(self):
        """
        Näyttää latausviestin käyttäjälle.
        """

        self.loading_label.config(text="Dataa ladataan, ole hyvä ja odota...")
        self._frame.update_idletasks()

    def load_data(self, train_size):
        """
        Lataa dataa DataLoader-luokan avulla ja jakaa sen koulutus- ja testiosiin.

        Args:
            train_size: Koulutusdatan kuvien määrä.
        """
        self.loader = DataLoader()
        self.loader.load_data()

        (self.train_data, self.test_data, self.train_target, self.test_target,
        self.train_point_lists, self.test_point_lists, self.train_binary_matrices,
        self.test_binary_matrices) = self.loader.split_data(train_size)

        self.select_test_image_count()

    def select_test_image_count(self):
        """
        Luo käyttöliittymän testikuvien määrän ja k-arvon valitsemiseksi.
        """

        # Poista edellinen sisältö
        for widget in self._frame.winfo_children():
            widget.destroy()

        # Testikuvien määrän valinta
        ttk.Label(master=self._frame, text="Valitse testikuvien määrä (1-50):").pack(pady=10)
        test_image_count_entry = ttk.Entry(master=self._frame, textvariable=self.test_image_count)
        test_image_count_entry.pack(pady=10)

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
        """
        Suorittaa ennusteen KNN-luokittelijalla perustuen käyttäjän syötteisiin ja näyttää tulokset.
        """
        try:
            test_image_count_str = self.test_image_count.get()
            k_str = self.k_value.get()

            if (not test_image_count_str.isdigit() or
                not k_str.isdigit()):
                raise ValueError("Kaikkien arvojen on oltava positiivisia kokonaislukuja.")

            test_image_count = int(test_image_count_str)
            k = int(k_str)

            if not 1 <= test_image_count <= 50:
                raise ValueError("Testikuvien määrän tulee olla välillä 1-50.")
            
            train_image_count = int(self.train_image_count.get())

            knn = KNN(k=k,
                      train_data=self.train_data[:train_image_count],
                      test_data=self.test_data,
                      train_labels=self.train_target[:train_image_count],
                      test_labels=self.test_target,
                      train_point_lists=self.train_point_lists[:train_image_count],
                      test_point_lists=self.test_point_lists,
                      train_binary_matrices=self.train_binary_matrices[:train_image_count],
                      test_binary_matrices=self.test_binary_matrices)

            (correct_predictions, incorrect_predictions, total_time,
             predictions, test_indices) = knn.run(test_image_count)

            results_view = ResultsView(
                            self._root, correct_predictions, incorrect_predictions,
                            total_time, test_indices, predictions, self.retry)

            results_view.pack()
            self._frame.destroy()

        except ValueError as e:
            self.result_label.config(text=f"Virhe: {str(e)}")

    def retry(self):
        """
        Käynnistää StartView-näkymän uudelleen käyttäjälle.
        """
        self._frame.destroy()
        start_view = StartView(self._root)
        start_view.pack()
