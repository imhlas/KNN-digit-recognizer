from ui.start_view import StartView

class UI:
    def __init__(self, root):
        self.root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _show_start_view(self):
        self._current_view = StartView(self.root)
        self._current_view.pack()