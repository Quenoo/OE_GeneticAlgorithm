import numpy as np


def random_x_diff_ints(start, end, times):
    cross_points = [np.random.randint(start, end) for _ in range(times)]
    if end - start > times: # if it is passible
        while len(set(cross_points)) != len(cross_points):
            cross_points = [np.random.randint(start, end) for _ in range(times)]
    return sorted(cross_points)


class Mutation:
    def __init__(self, decision, prob):
        self.decision = decision
        self.prob = prob

    def mutate(self, pop):
        if self.decision == 'one_point_mutation':
            return self.one_point_mutation(pop)
        if self.decision == 'two_point_mutation':
            return self.two_point_mutation(pop)
        if self.decision == 'edge_mutation':
            return self.edge_mutation(pop)
        else:
            raise NameError("Not a type of mutation")

    def one_point_mutation(self, pop):
        new_pop = []
        for i in range(len(pop)):
            roll = np.random.random()
            if roll < self.prob:
                mutation_p = np.random.randint(0, pop.shape[2])
                new_x = pop[i][0]
                new_y = pop[i][1]
                new_x[mutation_p] = 1 - new_x[mutation_p]
                new_y[mutation_p] = 1 - new_y[mutation_p]
                new_pop.append([new_x, new_y])
            else:
                new_pop.append(pop[i])
        return np.array(new_pop)

    def two_point_mutation(self, pop):
        new_pop = []
        for i in range(len(pop)):
            roll = np.random.random()
            if roll < self.prob:
                mutation_p1, mutation_p2 = random_x_diff_ints(0, pop.shape[2], 2)
                new_x = pop[i][0]
                new_y = pop[i][1]
                new_x[mutation_p1], new_x[mutation_p2] = 1 - new_x[mutation_p1], 1 - new_x[mutation_p2]
                new_y[mutation_p1], new_y[mutation_p2] = 1 - new_y[mutation_p1], 1 - new_y[mutation_p2]
                new_pop.append([new_x, new_y])
            else:
                new_pop.append(pop[i])
        return np.array(new_pop)

    def edge_mutation(self, pop):
        new_pop = []
        for i in range(len(pop)):
            roll = np.random.random()
            if roll < self.prob:
                new_x = pop[i][0]
                new_y = pop[i][1]
                new_x[-1] = 1 - new_x[-1]
                new_y[-1] = 1 - new_y[-1]
                new_pop.append([new_x, new_y])
            else:
                new_pop.append(pop[i])
        return np.array(new_pop)


if __name__ == '__main__':
    zeros = np.zeros(10)
    ones = np.ones(10)
    pop = np.array([[ones, zeros], [zeros, ones], [ones, zeros]])
    # pop_c = Mutation('one_point_mutation', 1).mutate(pop)
    # print(pop_c)
    # pop_c = Mutation('edge_mutation', 1).mutate(pop)
    pop_c = Mutation('two_point_mutation', 1).mutate(pop)
    print(pop_c)

