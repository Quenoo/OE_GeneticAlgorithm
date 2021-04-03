import numpy as np


def random_x_diff_ints(start, end, times):
    cross_points = [np.random.randint(start, end) for _ in range(times)]
    if end - start > times: # if it is passible
        while len(set(cross_points)) != len(cross_points):
            cross_points = [np.random.randint(start, end) for _ in range(times)]
    return sorted(cross_points)


class Inversion:
    def __init__(self, decision, prob):
        self.decision = decision
        self.prob = prob

    def inverse(self, pop):
        if self.decision == 'standard_inversion':
            return self.standard_inversion(pop)
        else:
            raise NameError("Not a type of inversion")

    def standard_inversion(self, pop):
        new_pop = []
        for i in range(len(pop)):
            roll = np.random.random()
            if roll < self.prob:
                new_x = pop[i][0]
                new_y = pop[i][1]

                mutation_p1, mutation_p2 = random_x_diff_ints(0, pop.shape[2], 2)
                for index in range(mutation_p1, mutation_p2 + 1):
                    new_x[index] = 1 - new_x[index]
                    new_y[index] = 1 - new_y[index]
                new_pop.append([new_x, new_y])
            else:
                new_pop.append(pop[i])
        return np.array(new_pop)


if __name__ == '__main__':
    zeros = np.zeros(10)
    ones = np.ones(10)
    pop = np.array([[ones, zeros], [zeros, ones], [zeros, ones]])
    pop_c = Inversion('standard_inversion', 1).inverse(pop)
    print(pop_c)