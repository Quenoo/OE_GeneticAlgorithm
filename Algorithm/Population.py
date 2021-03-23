import numpy as np


class Population:
    def __init__(self, function, population_size, num_of_variables, range_min, range_max, precision):
        self.function = function
        self.population_size = population_size
        self.num_of_variables = num_of_variables
        self.range_min = range_min
        self.range_max = range_max
        self.precision = precision
        self.num_of_bits = self.binary_lenght()

    def to_dec(self, li): # takes numpy array, returns decimal represntation
        li = ''.join(str(int(e)) for e in li)
        return int(li, 2)

    def binary_lenght(self):
        a = self.range_min
        b = self.range_max
        d = self.precision
        return int(np.ceil(np.log2((b - a) * (10 ** d)) + np.log2(1)))

    def generate_population(self):
        return np.random.randint(2, size=(self.population_size, self.num_of_variables, self.num_of_bits))

    def binary_to_decimal(self, chromosomes):
        a = self.range_min
        b = self.range_max
        # d = self.precision
        m = self.num_of_bits
        decimal = []
        for i in range(0, len(chromosomes)):
            decimal_bin_x1 = self.to_dec(chromosomes[i][0])
            x1 = a + decimal_bin_x1 * (b - a) / (2 ** m - 1)
            decimal_bin_x2 = self.to_dec(chromosomes[i][1])
            x2 = a + decimal_bin_x2 * (b - a) / (2 ** m - 1)
            decimal.append((x1, x2))
        return decimal


if __name__ == '__main__':
    pop = Population(lambda x: x**2, 5, 2, -1, 1, 6)
    p = pop.generate_population()
    decoded = pop.binary_to_decimal(p)
    print(decoded)
    pass

