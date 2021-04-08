from Function import booth_function
from Population import *


def new_pop_from_indexes(pop, indexes):
    return np.array([pop[i] for i in indexes])


class Selection:
    def __init__(self, decision, percentage):
        self.decision = decision
        self.percentage = percentage

    def select(self, pop, evaluated_pop):
        if self.decision == 'best':
            return self.best(pop, evaluated_pop, self.percentage)
        if self.decision == 'roulette_wheel':
            return self.roulette_wheel(pop, evaluated_pop, self.percentage)
        if self.decision == 'tournament':
            return self.tournament(pop, evaluated_pop, self.percentage)
        else:
            raise NameError("Not a type of selection")

    def best(self, pop, evaluated_pop, percentage):
        pop_size = pop.shape[0]
        not_selected_indexes = [i for i in range(pop_size)]

        n_selected = int(evaluated_pop.size * (percentage / 100))
        selected_indexes = evaluated_pop.argsort()[:n_selected]
        selected = new_pop_from_indexes(pop, selected_indexes)

        not_selected_indexes = [i for i in not_selected_indexes if i not in selected_indexes]
        not_selected = new_pop_from_indexes(pop, not_selected_indexes)

        return selected, not_selected

    def roulette_wheel(self, pop, evaluated_pop, percentage):
        pop_size = pop.shape[0]
        total = np.insert(np.cumsum(1 / evaluated_pop), 0, 0)
        rng = np.random.default_rng()

        n_selected = int(evaluated_pop.size * (percentage / 100))
        selected = []
        counter = 0
        i = 1

        while counter < n_selected:
            if i == total.size:
                i = i - 1

            prev = total[i - 1] / total[-1]
            curr = total[i] / total[-1]

            if prev <= rng.random() < curr:
                selected.append(pop[i - 1])
                counter += 1
                i = 1
            else:
                i += 1

        not_selected = [pop[np.random.randint(0, pop_size)] for _ in range(pop.size - n_selected)]

        return np.array(selected), np.array(not_selected)

    def tournament(self, pop, evaluated_pop, percentage):
        pop_size = pop.shape[0]
        k = pop_size // (int((percentage / 100) * pop_size))
        not_selected_indexes = [i for i in range(pop_size)]

        selected_indexes = np.array([i for i in range(len(evaluated_pop))])
        np.random.shuffle(selected_indexes)
        selected_indexes = np.array_split(selected_indexes, int(len(evaluated_pop) / k))

        selected_indexes = list(map(lambda x: min(x, key=lambda y: evaluated_pop[y]), selected_indexes))
        selected = new_pop_from_indexes(pop, selected_indexes)

        not_selected_indexes = [i for i in not_selected_indexes if i not in selected_indexes]
        not_selected = new_pop_from_indexes(pop, not_selected_indexes)

        return selected, not_selected


if __name__ == '__main__':
    pop = Population(booth_function, 100, 2, -1, 1, 6)
    p = pop.generate_population()
    evaluated = pop.evaluate_population(p)

    pop_best = Selection('best', 20).select(p, evaluated)
    print(f"20% from best selection:\n{pop.decode_population(pop_best[0])}")
    pop_roulette = Selection('roulette_wheel', 20).select(p, evaluated)
    print(f"\n\n20% from roulette selection:\n{pop.decode_population(pop_roulette[0])}")
    pop_tournament = Selection('tournament', 20).select(p, evaluated)
    print(f"\n\n20% from tournament selection:\n{pop.decode_population(pop_tournament[0])}")

