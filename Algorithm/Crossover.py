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
                cross_p = np.random.randint(1, pop.shape[2])

                new_x1 = np.concatenate([pop[i][0][:cross_p], pop[i + 1][0][cross_p:]])
                new_x2 = np.concatenate([pop[i + 1][0][:cross_p], pop[i][0][cross_p:]])

                new_y1 = np.concatenate([pop[i][1][:cross_p], pop[i + 1][1][cross_p:]])
                new_y2 = np.concatenate([pop[i + 1][1][:cross_p], pop[i][1][cross_p:]])

                new_pop.append([new_x1, new_y1])
                new_pop.append([new_x2, new_y2])
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i+1])
        return np.array(new_pop)

    def two_point_cross(self, pop):
        new_pop = []
        pop_size = pop.shape[0]
        if pop_size % 2 != 0:
            end = pop.shape[0] - 1
        else:
            end = pop.shape[0]
        for i in range(0, end, 2):
            roll = np.random.random()
            if roll < self.prob:
                cross_p1 = np.random.randint(1, pop.shape[1])
                cross_p2 = np.random.randint(1, pop.shape[1])
                if cross_p2 == cross_p1:
                    pass


                # new_chrom_1 = np.concatenate([pop[i][:cross_p], pop[i + 1][cross_p:]])
                # new_chrom_2 = np.concatenate([pop[i + 1][:cross_p], pop[i][cross_p:]])
                # new_pop.append(new_chrom_1)
                # new_pop.append(new_chrom_2)
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i+1])
        return np.array(new_pop)


if __name__ == '__main__':
    pop = np.array([[[1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 1, 1]]])
    pop_c = Crossover('one_point_cross', 1).one_point_cross(pop)
    print(pop_c)