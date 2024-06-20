import tkinter as tk
from tkinter import ttk, constants

class ResultsView:
    def __init__(self, root, correct_predictions, incorrect_predictions, total_time, test_indices, predictions, retry_callback):
        self._root = root
        self._frame = None
        self.correct_predictions = correct_predictions
        self.incorrect_predictions = incorrect_predictions
        self.total_time = total_time
        self.test_indices = test_indices
        self.predictions = predictions
        self.retry_callback = retry_callback

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=constants.BOTH, expand=True)

        ttk.Label(master=self._frame, text=f"Oikein ennustettuja kuvia: {self.correct_predictions}").pack(pady=10)
        ttk.Label(master=self._frame, text=f"Väärin ennustettuja kuvia: {self.incorrect_predictions}").pack(pady=10)
        ttk.Label(master=self._frame, text=f"Laskentaan käytetty kokonaisaika: {self.total_time:.4f} sekuntia").pack(pady=10)

        # Taulukko testikuvista ja ennusteista
        columns = ("#1", "#2", "#3")
        tree = ttk.Treeview(master=self._frame, columns=columns, show="headings", selectmode="none")
        tree.heading("#1", text="Oikea arvo")
        tree.heading("#2", text="Ennuste")
        tree.heading("#3", text="Naapurit")

        # Keskittää arvot sarakkeissa
        tree.column("#1", anchor="center")
        tree.column("#2", anchor="center")
        tree.column("#3", anchor="center")

        for i, (test_label, predicted_label, neighbors) in enumerate(self.predictions):
            neighbors_str = ', '.join(map(str, neighbors))
            tree.insert("", "end", values=(test_label, predicted_label, neighbors_str))

        tree.pack(pady=10, fill=constants.BOTH, expand=True)

        # Ennusta uudestaan -painike
        retry_button = ttk.Button(master=self._frame, text="Ennusta uudestaan", command=self.retry)
        retry_button.pack(pady=10)

        # Sulje-painike
        close_button = ttk.Button(master=self._frame, text="Sulje", command=self._root.quit)
        close_button.pack(pady=10)

    def retry(self):
        self._frame.destroy()
        self.retry_callback()
