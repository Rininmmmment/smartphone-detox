class DisplayManager:
    def __init__(self, display_driver=None, width=200, height=200):
        self.display_driver = display_driver
        self.width = width
        self.height = height

    def show_text(self, lines: list):
        pass

    def show_graph(self, data):
        pass

    def clear(self):
        pass
