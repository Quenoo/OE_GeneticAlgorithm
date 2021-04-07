import numpy as np


class Files:
    @staticmethod
    def numpy_to_csv(array, file_name):
        file_name = '../Data/' + file_name
        np.savetxt(file_name, array, delimiter=",")


if __name__ == '__main__':
    Files.numpy_to_csv(np.array([1, 2, 3, 4]), 'data')
