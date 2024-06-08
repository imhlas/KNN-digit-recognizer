from tkinter import Tk, ttk
from ui.ui import UI

def main():

    window = Tk()
    window.title("KNN-digit-recognizer")
    window.geometry("600x400") 

    style = ttk.Style()
    style.configure("Selected.TButton", background="darkgrey")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()