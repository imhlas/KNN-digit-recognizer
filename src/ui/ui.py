from ui.start_view import StartView

class UI:
    def __init__(self, root):
        """
        Alustaa UI-luokan.
        """
        self.root = root
        self._current_view = None

    def start(self):
        """
        Käynnistää käyttöliittymän ja näyttää aloitusnäkymän.
        """
        self._show_start_view()

    def _show_start_view(self):
        """
        Luo ja näyttää aloitusnäkymän (StartView).
        """
        self._current_view = StartView(self.root)
        self._current_view.pack()