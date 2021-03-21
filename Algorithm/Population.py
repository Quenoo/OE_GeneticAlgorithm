import numpy as np


class Population:
    def __init__(self, function, population_size, range_min, range_max, precision, num_of_variables = 2):
        self.function = function
        self.population_size = population_size
        self.range_min = range_min
        self.range_max = range_max
        self.precision = precision
        self.num_of_variables = num_of_variables
        self.num_of_bits = self.get_num_of_bits()
        self.chromosomes = self.generate_population()

    def get_num_of_bits(self):
        return ((self.range_max - self.range_min) // self.precision).bit_length()

    def generate_population(self):
        return np.random.randint(2, size = (self.population_size, self.num_of_variables, self.precision))

    def decode_population(self):
        self.chromosomes = ChromosomeCodec.decode_chromosomes(self.chromosomes, self.range_min, self.range_max, self.precision)

    def encode_population(self):
        self.chromosomes = ChromosomeCodec.encode_chromosomes(self.chromosomes, self.range_min, self.range_max, self.precision)

def to_binary(number, length):
    binary = []

    while num != 0:
        bit = num % 2
        binary.append(bit)
        num = num // 2
    
    binary.reverse()
    
    while len(binary) != m:
        binary.insert(0, 0)
    
    return binary


def to_decimal(bits):
    result = 0

    for bit in bits:
        result = (result << 1) | bit

    return result

class ChromosomeCodec:
    @staticmethod
    def encode_chromosomes(chromosomes, a, b, d):
        m = np.ceil(np.log2((b - a) * (10 ** d)) + np.log2(1))
        binary = []

        for i in range(0, len(chromosomes)):
            x1 = np.round((chromosomes[i][0] - a) / ((b - a) / ((2 ** m) - 1)))
            x2 = np.round((chromosomes[i][1] - a) / ((b - a) / ((2 ** m) - 1)))
            binary.append((to_binary(int(x1), m), to_bin(int(x2), m)))

        return binary

    @staticmethod
    def decode_chromosomes(chromosomes, a, b, d):
        m = np.ceil(np.log2((b - a) * (10 ** d)) + np.log2(1))
        decimal = []

        for i in range(0, len(chromosomes)):
            x1 = a + to_decimal(chromosomes[i][0]) * (b - a) / (2 ** m - 1)
            x2 = a + to_decimal(chromosomes[i][1]) * (b - a) / (2 ** m - 1)
            decimal.append((x1, x2))

        return decimal