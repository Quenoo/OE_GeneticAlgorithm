import os
import numpy as np


class Files:
    @staticmethod
    def numpy_to_csv(array, file_name):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_name = current_folder + '/../Data/' + file_name
        np.savetxt(file_name, array, delimiter=",")


if __name__ == '__main__':
    Files.numpy_to_csv(np.array([1, 2, 3, 4]), 'data.csv')
