from PyQt5.QtWidgets import QApplication


class App:
    def __init__(self):
        self.__app = QApplication([])
        self.gui = Gui()
        self.__app.exec_()