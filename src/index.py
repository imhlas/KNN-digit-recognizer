"""
Tämä moduuli käynnistää KNN-numerontunnistussovelluksen käyttöliittymän käyttäen tkinter-kirjastoa.

Moduuli luo pääikkunan, määrittää sen tyylit ja käynnistää käyttöliittymän,
joka hallinnoi eri näkymiä numerontunnistuksen
toiminnallisuuksien suorittamiseen.
"""

from tkinter import Tk, ttk
from ui.ui import UI

def main():
    """
    Sovelluksen pääfunktio, joka käynnistää käyttöliittymän.
    """

    window = Tk()
    window.title("KNN-digit-recognizer")
    window.geometry("800x600")

    style = ttk.Style()
    style.configure("Selected.TButton", background="darkgrey")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
