import tkinter as tk
from tkinter import ttk, constants
from PIL import Image, ImageTk
import numpy as np
import random
from data_loader import MNISTLoader

class StartView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self.loader = MNISTLoader()
        self.data, self.target = self.loader.load_data()

        self._initialize()
        self._show_random_image() 

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self.label = ttk.Label(master=self._frame, text="Satunnainen numero MNIST-datasta")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.image_label = tk.Label(master=self._frame)
        self.image_label.grid(row=1, column=0, padx=10, pady=10)

        self.random_button = ttk.Button(master=self._frame, text="Näytä uusi numero", command=self._show_random_image)
        self.random_button.grid(row=2, column=0, padx=10, pady=10)

    def _show_random_image(self):
        self.current_image_index = random.randint(0, len(self.data) - 1)
        image_data = self.data[self.current_image_index].reshape(28, 28).astype(np.uint8)

        img = Image.fromarray(image_data)
        imgtk = ImageTk.PhotoImage(image=img)
        self.image_label.config(image=imgtk)
        self.image_label.image = imgtk 