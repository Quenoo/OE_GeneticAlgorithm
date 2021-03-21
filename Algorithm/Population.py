import numpy as np


class Population:
    def __init__(self, function, population_size, num_of_variables, range_min, range_max, precision):
        self.function = function
        self.population_size = population_size
        self.num_of_variables = num_of_variables
        self.range_min = range_min
        self.range_max = range_max
        self.precision = precision
        self.num_of_bits = self.get_num_of_bits()
        self.new_step = self.new_step()

    def get_num_of_bits(self):
        return int((self.range_max - self.range_min) / self.precision).bit_length()

    def generate_population(self):
        return np.random.randint(2, size=(self.population_size, self.num_of_variables * self.num_of_bits))

    def decode_individual(self, individual):
        temp = individual.reshape((self.num_of_variables, self.num_of_bits))
        decode_individual = np.ndarray(self.num_of_variables)
        vector = []
        for i in range(0, self.num_of_bits):
            vector.insert(0, 2 ** i)
            