from PyQt5.QtWidgets import QApplication

from Gui import Gui


class App:
    def __init__(self):
        self.__app = QApplication([])
        self.gui = Gui()
        self.__app.exec_()