import numpy as np


class EliteStrategy:
    def __init__(self, percentage):
        self.percentage = percentage

    def elite(self, pop, fitness):
        if self.percentage == 0:
            return np.array([])
        pop_size = pop.shape[0]

        n_selected = int(pop_size * self.percentage)
        selected_indexes = fitness.argsort()[:n_selected] # to reverse sort (highest to lowest)
        selected = pop[selected_indexes]
        return selected


if __name__ == '__main__':
    pop = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
    ])
    fit = np.array([102, 1, 21])
    eli = EliteStrategy(0.9)
    p = eli.elite(pop, fit)
    print(p)