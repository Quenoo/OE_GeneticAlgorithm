import numpy as np


def random_x_diff_ints(start, end, times):
    cross_points = [np.random.randint(start, end) for _ in range(times)]
    if end - start > times: # if it is passible
        while len(set(cross_points)) != len(cross_points):
            cross_points = [np.random.randint(start, end) for _ in range(times)]
    return sorted(cross_points)


class Crossover:
    def __init__(self, decision, prob):
        self.decision = decision
        self.prob = prob

    def cross(self, pop):
        if self.decision == 'one_point_cross':
            return self.one_point_cross(pop)
        if self.decision == 'two_point_cross':
            return self.two_point_cross(pop)
        if self.decision == 'three_point_cross':
            return self.three_point_cross(pop)
        if self.decision == 'homogenous_cross':
            return self.homogenous_cross(pop)
        else:
            raise NameError("Not a type of crossover")

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

                cross_p = random_x_diff_ints(0, pop.shape[2], 1)[0]
                # print(cross_p)

                pop_1_x, pop_1_y = pop[i][0], pop[i][1]
                pop_2_x, pop_2_y = pop[i+1][0], pop[i+1][1]

                new_x1 = np.concatenate([
                    pop_1_x[:cross_p], pop_2_x[cross_p:]
                ])
                new_x2 = np.concatenate([
                    pop_2_x[:cross_p], pop_1_x[cross_p:]
                ])

                new_y1 = np.concatenate([
                    pop_1_y[:cross_p], pop_2_y[cross_p:]
                ])
                new_y2 = np.concatenate([
                    pop_2_y[:cross_p], pop_1_y[cross_p:]
                ])

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
                cross_p1, cross_p2 = random_x_diff_ints(1, pop.shape[2], 2)

                # while cross_p1 == cross_p2:
                #     cross_p2 = np.random.randint(1, pop.shape[2])
                # print(cross_p1, cross_p2)

                pop_1_x, pop_1_y = pop[i][0], pop[i][1]
                pop_2_x, pop_2_y = pop[i+1][0], pop[i+1][1]

                new_x1 = np.concatenate([
                    pop_1_x[:cross_p1], pop_2_x[cross_p1:cross_p2], pop_1_x[cross_p2:]
                ])
                new_x2 = np.concatenate([
                    pop_2_x[:cross_p1], pop_1_x[cross_p1:cross_p2], pop_2_x[cross_p2:]
                ])

                new_y1 = np.concatenate([
                    pop_1_y[:cross_p1], pop_2_y[cross_p1:cross_p2], pop_1_y[cross_p2:]
                ])
                new_y2 = np.concatenate([
                    pop_2_y[:cross_p1], pop_1_y[cross_p1:cross_p2], pop_2_y[cross_p2:]
                ])

                new_pop.append([new_x1, new_y1])
                new_pop.append([new_x2, new_y2])
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i+1])
        return np.array(new_pop)

    def three_point_cross(self, pop):
        new_pop = []
        pop_size = pop.shape[0]
        if pop_size % 2 != 0:
            end = pop.shape[0] - 1
        else:
            end = pop.shape[0]
        for i in range(0, end, 2):
            roll = np.random.random()
            if roll < self.prob:
                cross_p1, cross_p2, cross_p3 = random_x_diff_ints(1, pop.shape[2], 3)

                # print(cross_p1, cross_p2, cross_p3)

                pop_1_x, pop_1_y = pop[i][0], pop[i][1]
                pop_2_x, pop_2_y = pop[i+1][0], pop[i+1][1]

                new_x1 = np.concatenate([
                    pop_1_x[:cross_p1], pop_2_x[cross_p1:cross_p2], pop_1_x[cross_p2:cross_p3], pop_2_x[cross_p3:]
                ])
                new_x2 = np.concatenate([
                    pop_2_x[:cross_p1], pop_1_x[cross_p1:cross_p2], pop_2_x[cross_p2:cross_p3], pop_1_x[cross_p3:]
                ])
                new_y1 = np.concatenate([
                    pop_1_y[:cross_p1], pop_2_y[cross_p1:cross_p2], pop_1_y[cross_p2:cross_p3], pop_2_y[cross_p3:]
                ])
                new_y2 = np.concatenate([
                    pop_2_y[:cross_p1], pop_1_y[cross_p1:cross_p2], pop_2_y[cross_p2:cross_p3], pop_1_y[cross_p3:]
                ])

                new_pop.append([new_x1, new_y1])
                new_pop.append([new_x2, new_y2])
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i+1])
        return np.array(new_pop)

    def homogenous_cross(self, pop):
        new_pop = []
        pop_size = pop.shape[0]
        if pop_size % 2 != 0:
            end = pop.shape[0] - 1
        else:
            end = pop.shape[0]
        for i in range(0, end, 2):
            roll = np.random.random()
            if roll < self.prob:

                pop_1_x, pop_1_y = pop[i][0], pop[i][1]
                pop_2_x, pop_2_y = pop[i + 1][0], pop[i + 1][1]

                new_x1 = [pop_1_x[i] if i % 2 == 0 else pop_2_x[i] for i in range(pop_1_x.shape[0])]
                new_x2 = [pop_2_x[i] if i % 2 == 0 else pop_1_x[i] for i in range(pop_1_x.shape[0])]
                new_y1 = [pop_1_y[i] if i % 2 == 0 else pop_2_y[i] for i in range(pop_1_x.shape[0])]
                new_y2 = [pop_2_y[i] if i % 2 == 0 else pop_1_y[i] for i in range(pop_1_x.shape[0])]
                new_pop.append([new_x1, new_y1])
                new_pop.append([new_x2, new_y2])
            else:
                new_pop.append(pop[i])
                new_pop.append(pop[i + 1])
        return np.array(new_pop)


if __name__ == '__main__':
    zeros = np.zeros(10)
    ones = np.ones(10)
    pop = np.array([[ones, zeros], [zeros, ones]])
    pop_c = Crossover('one_point_cross', 1).cross(pop)
    print(pop_c)
    pop_2c = Crossover('two_point_cross', 1).cross(pop)
    print(pop_2c)
    pop_3c = Crossover('three_point_cross', 1).cross(pop)
    print(pop_3c)
    pop_homo = Crossover('homogenous_cross', 1).cross(pop)
    print("\n\n", pop_homo)
