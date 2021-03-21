import numpy as np

from Function import booth_function
from Evaluation import evaluate_population


class Selection:
    def return_chosen_method(method, population, percentage):
        if (method == 'best'):
            return best(population, percentage)
        else if (method == 'roulette_wheel'):
            return roulette_wheel(population, percentage)
        else if (method == 'tournament'):
            return tournament(population, percentage)
        else:
            pass

    def best(population, percentage):
        evaluated_population = evaluate_population(population, booth_function)
        sorted_population = np.sort(evaluated_population) # from lowest, as the function has a minimum at 0
        new_population, rest = np.split(sorted_population, int(len(sorted_population) * percentage))

        return new_population

    def roulette_wheel(population, percentage):
        evaluated_population = evaluate_population(population, booth_function)
        fitness_population = 1 / evaluate_population(population)
        fitness_sum = np.sum(evaluated_population)

        probabilities = np.array(len(population))

        for individual in fitness_population:
            np.append(probabilities, individual / fitness_sum)

        distribuants = np.cumsum(probabilities)

        new_population = []
        random = np.random.rand()

        for i, value in distribuants:
            if value > random:
                new_population.append(fitness_population[i])
                break

        return new_population

    def tournament(population, percentage):
        tournament_size = (int(len(population) * percentage))

        evaluated_population = evaluate_population(population, booth_function)
        groups = np.array_split(evaluated_population, tournament_size)

        new_population = np.empty(len(population) // tournament_size)

        for group in groups:
            np.append(new_population, np.min(group))
        
        return new_population