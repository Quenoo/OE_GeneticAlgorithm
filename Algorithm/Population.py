import numpy as np


class Population:
    def __init__(self, function, population_size, num_of_variables, range_min, range_max, precision):
        self.function = function
        self.population_size = population_size
        self.num_of_variables = num_of_variables
        self.range_min = range_min
        self.range_max = range_max
        self.precision = precision
        self.num_of_bits = self.binary_length()

    def np_to_dec(self, li): # takes numpy array, returns decimal represntation
        li = ''.join(str(int(e)) for e in li)
        return int(li, 2)

    def binary_length(self):
        a = self.range_min
        b = self.range_max
        d = self.precision
        return int(np.ceil(np.log2(float((b - a) * (10 ** d))) + np.log2(1)))

    def generate_population(self):
        return np.random.randint(2, size=(self.population_size, self.num_of_variables, self.num_of_bits))

    def decode_population(self, population):
        a = self.range_min
        b = self.range_max
        m = self.num_of_bits
        decoded = []
        for i in range(0, len(population)):
            x1_bin_part = self.np_to_dec(population[i][0])
            x1 = a + x1_bin_part * (b - a) / (2 ** m - 1)
            x2_bin_part = self.np_to_dec(population[i][1])
            x2 = a + x2_bin_part * (b - a) / (2 ** m - 1)
            decoded.append([x1, x2])
        return np.array(decoded)

    def evaluate_population(self, population):
        population = self.decode_population(population)
        return np.array([self.function(x1, x2) for x1, x2 in population])


if __name__ == '__main__':
    pop = Population(lambda x1, x2: x1 + x2, 5, 2, -1, 1, 6)
    p = pop.generate_population()
    print(f"Generated population:\n{p}")
    evaluated = pop.evaluate_population(p)
    print(f"\nEvaluated population:\n{evaluated}")
    decoded = pop.decode_population(p)
    print(f"\nDecoded population:\n{decoded}")
