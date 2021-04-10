import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QPixmap, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QLabel, QFormLayout, QLineEdit, QWidget, QComboBox, QPushButton, QMessageBox

from Algorithm import Algorithm
from OutputGenerators.Files import Files


class App:
    def __init__(self):
        self.app = QApplication([])
        self.window = MainWindow()
        self.app.exec_()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genetic algorithm 1: Booth function minimization")
        self.layout = QFormLayout()

        self.set_image()
        self.set_configuration_inputs()
        self.add_run_button()

        self.setLayout(self.layout)
        self.show()

    def set_image(self):
        label = QLabel()
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_name = current_folder + '/booth.png'
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignLeft)

        self.layout.addWidget(label)

    def set_configuration_inputs(self):
        epochs_input = QLineEdit()
        epochs_input.setPlaceholderText("Epochs")
        epochs_input.setValidator(QIntValidator(1, 1000))

        self.layout.addRow(epochs_input)

        self.set_configuration_inputs_population()
        self.set_configuration_inputs_operations()

    def set_configuration_inputs_population(self):
        population_size_input = QLineEdit()
        population_size_input.setPlaceholderText("Population size")
        population_size_input.setValidator(QIntValidator(1, 10000))

        population_precision_input = QLineEdit()
        population_precision_input.setPlaceholderText("Precision of the population's binary representation")
        population_precision_input.setValidator(QIntValidator(1, 100))

        self.layout.addRow(population_size_input)
        self.layout.addRow(population_precision_input)

    def set_configuration_inputs_operations(self):
        # selection, crossing, mutation, inversion
        self.add_operation_input("Selection method", ['best', 'roulette_wheel', 'tournament'])
        self.add_operation_input("Crossover method", ['one_point_cross', 'two_point_cross', 'three_point_cross',
                                                      'homogenous_cross'])
        self.add_operation_input("Mutation method", ['one_point_mutation', 'two_point_mutation', 'edge_mutation'])
        self.add_operation_input("Inversion method", ['standard_inversion'])

        self.add_operation_param("Selection percentage")
        self.add_operation_param("Crossover probability")
        self.add_operation_param("Mutation probability")
        self.add_operation_param("Inversion probability")
        self.add_operation_param("Elite strategy percentage")

    def add_operation_input(self, label_text, items):
        label = QLabel()
        label.setText(label_text)

        operation_box = QComboBox()
        operation_box.addItems(items)

        self.layout.addRow(label)
        self.layout.addRow(operation_box)

    def add_operation_param(self, label_text):
        param_input = QLineEdit()
        param_input.setPlaceholderText(label_text)
        param_input.setValidator(QDoubleValidator(0.0, 1.0, 2))

        self.layout.addRow(param_input)

    def add_run_button(self):
        button = QPushButton("Run algorithm")
        button.clicked.connect(lambda: self.button_pressed())

        self.layout.addRow(button)

    def text_at(self, index):
        return self.layout.itemAt(index).widget().text()

    def combobox_text_at(self, index):
        return self.layout.itemAt(index).widget().currentText()

    def input_to_float(self, input_text):
        return float(input_text.replace(',', '.'))

    def get_last_individual(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_name = current_folder + '/../Data/best_individual.csv'

        with open(file_name, "rb") as f:
            last = Files.tail(f).decode('utf-8')

        return tuple(last.rstrip('\n').split(','))

    def button_pressed(self):
        params = {
            'epochs':               int(self.text_at(1)),
            'population_size':      int(self.text_at(2)),
            'population_precision': int(self.text_at(3)),
            'selection_type':       self.combobox_text_at(5),
            'crossover_type':       self.combobox_text_at(7),
            'mutation_type':        self.combobox_text_at(9),
            'inversion_type':       self.combobox_text_at(11),
            'selection_prob':       self.input_to_float(self.text_at(12)),
            'crossover_prob':       self.input_to_float(self.text_at(13)),
            'mutation_prob':        self.input_to_float(self.text_at(14)),
            'inversion_prob':       self.input_to_float(self.text_at(15)),
            'elite_prob':           self.input_to_float(self.text_at(16))
        }

        time_execution = Algorithm(params).run()

        x1, x2 = self.get_last_individual()

        msg = QMessageBox()
        msg.setWindowTitle("Wynik")
        msg.setText(f"Algorytm zajął {time_execution:.4f} sekund\nNajlepszy osobnik z ostatniej epoki:\n"
                    f"{float(x1):.8f}, {float(x2):.8f}")

        msg.exec_()


if __name__ == '__main__':
    App()
