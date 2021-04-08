from Crossover import *
from Mutation import *
from Inversion import *
from OutputGenerators.Files import Files
from OutputGenerators.Plots import Plot
from Selection import *
from EliteStrategy import *
import time


class Algorithm:
    def __init__(self,
                 epochs=1000,
                 crossover_type=Crossover('one_point_cross', 0.6),
                 population=Population(booth_function, 100, 2, -10, 10, 6),
                 mutation_type=Mutation('one_point_mutation', 0.1),
                 inversion_type=Inversion('standard_inversion', 0.05),
                 selection_type=Selection('best', 20),
                 elite_strategy=EliteStrategy(0.1)):
        self.epochs = epochs
        self.Crossover = crossover_type
        self.Population = population
        self.Mutation = mutation_type
        self.Inversion = inversion_type
        self.Selection = selection_type
        self.EliteStrategy = elite_strategy

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
            # elite = self.EliteStrategy.elite(pop, fitness)
            # wybierz gatunki do crossowania (selection)
            selected, not_selected = self.Selection.select(pop, fitness)
            # krzyzowanie gatunków (cross)
            pop = self.Crossover.cross(selected)
            pop = np.concatenate((pop, not_selected), axis=0)
            # mutacja i/lub inversja
            pop = self.Mutation.mutate(pop)
            pop = self.Inversion.inverse(pop)
        time_execution = time.time() - time_start
        print(f"Algorytm zajął {time_execution:.3f} sekund")

        Plot.draw_save_plot(best_value, 'Wartość funkcji', 'Numer epoki',
                            'Wykres wartości funkcji dla najlepszych osobników', 'best_individual')
        Plot.draw_save_plot(avg_value, 'Wartość funkcji', 'Numer epoki',
                            'Wykres średniej wartości funkcji dla populacji', 'avg_pop')
        Plot.draw_save_plot(std_avg_value, 'Wartość odchylenia standardowego', 'Numer epoki',
                            'Wykres odchylenia standardowego dla populacji', 'avg_std_pop')
        Files.numpy_to_csv(best_individual, 'best_individual.csv')




if __name__ == '__main__':
    Algorithm().run()
