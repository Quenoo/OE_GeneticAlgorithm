from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        # TODO: initialize configuration fields, pass values to algorithm, show results, plots and execution time
        self.show()

    def init_window():
        window = QMainWindow()
        window.setWindowTitle("Genetic algorithm")
        window.show()