import numpy as np


class Crossover:
    def __init__(self, decision, prob):
        self.decision = decision
        self.prob = prob

    def cross(self, pop):
        if self.decision == 'one_point_cross':
            return self.one_point_cross(pop)
        else: pass

    def one_point_cross(self, pop):
        new_pop = []
        pop_size = pop.shape[0]
        if pop_size % 2 != 0:
            end = pop.shape[0] - 1
        else:
            end = pop.shape[0]
        for i in range(0, end, 2):
            roll = np.random.random()
            if roll < self.prob:
                cross_p = np.random.randint(1, pop.shape[1])
                new_chrom_1 = np.concatenate([pop[i][:cross_p], pop[i + 1][cross_p:]])
                new_chrom_2 = np.concatenate([pop[i + 1][:cross_p], pop[i][cross_p:]])
                new_pop.append(new_chrom_1)
                new_pop.append(new_chrom_2)
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i+1])
        return np.array(new_pop)
