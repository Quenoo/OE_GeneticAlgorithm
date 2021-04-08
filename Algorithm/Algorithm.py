from Crossover import *
from Mutation import *
from Inversion import *
from OutputGenerators.Files import Files
from OutputGenerators.Plots import Plot
from Selection import *
from EliteStrategy import *
import time


class Algorithm:
    def __init__(self, params):
        self.epochs = params['epochs']
        self.Crossover = Crossover(params['crossover_type'], params['crossover_prob'])
        self.Population = Population(booth_function, params['population_size'], 2, -10, 10,
                                     params['population_precision'])
        self.Mutation = Mutation(params['muataion_type'], params['muataion_prob'])
        self.Inversion = Inversion(params['inversion_type'], params['inversion_prob'])
        self.Selection = Selection(params['selection_type'], params['selection_prob'])
        self.EliteStrategy = EliteStrategy(params['elite_prob'])

    def run(self):
        best_value = []
        avg_value = []
        std_avg_value = []
        best_individual = []

        pop = self.Population.generate_population()
        time_start = time.time()
        for _ in range(self.epochs):
            # dla kazdej epoki
            # ocen populacje (evaluate)
            fitness = self.Population.evaluate_population(pop)

            # zapisz wartosci do wygenerowania wykresow
            best_value.append(fitness.min())
            avg_value.append(fitness.mean())
            std_avg_value.append(fitness.std())
            index_best = fitness.argsort()[0]
            best_individual.append(self.Population.decode_population(pop)[index_best])

            # zapisz % najlepszych (strategia elitarna)
            elite = self.EliteStrategy.elite(pop, fitness)
            # wybierz gatunki do crossowania (selection)
            selected, not_selected = self.Selection.select(pop, fitness)
            # krzyzowanie gatunków (cross)
            pop = self.Crossover.cross(selected)
            # mutacja i/lub inversja
            pop = self.Mutation.mutate(pop)
            pop = self.Inversion.inverse(pop)
            # jezeli strategia elitarna jest uzywana
            if elite.shape[0] != 0:
                #  polacz najlepszy % z populacja
                pop = np.concatenate((pop[:-elite.shape[0]], not_selected)) # , axis=0

        time_execution = time.time() - time_start
        print(f"Algorytm zajął {time_execution:.3f} sekund")

        Plot.draw_save_plot(best_value, 'Numer epoki', 'Wartość funkcji',
                            'Wykres wartości funkcji dla najlepszych osobników', 'best_individual')
        Plot.draw_save_plot(avg_value, 'Numer epoki', 'Wartość funkcji',
                            'Wykres średniej wartości funkcji dla populacji', 'avg_pop')
        Plot.draw_save_plot(std_avg_value, 'Numer epoki', 'Wartość odchylenia standardowego',
                            'Wykres odchylenia standardowego dla populacji', 'avg_std_pop')
        Files.numpy_to_csv(best_individual, 'best_individual.csv')


if __name__ == '__main__':
    params = {
        'epochs': 100,
        'crossover_type': 'one_point_cross',
        'crossover_prob': 0.6,
        'population_size': 10,
        'population_precision': 6,
        'muataion_type': 'one_point_mutation',
        'muataion_prob': 0.1,
        'inversion_type': 'standard_inversion',
        'inversion_prob': 0.05,
        'selection_type': 'best',
        'selection_prob': 80,
        'elite_prob': 0.1
    }
    Algorithm(params).run()
