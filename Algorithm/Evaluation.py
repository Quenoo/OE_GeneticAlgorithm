import numpy as np


def evaluate_population(population, function):
    return np.array(map(function, population))