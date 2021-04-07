# from Algorithm.Population import *
from Crossover import *
from Function import booth_function
from Population import *
from Mutation import *
from Inversion import *
from Selection import *
from EliteStrategy import *
from OutputGenerators.Files import *
from OutputGenerators.Plots import *
import time
# from Algorithm.Crossover import Crossover
# from Algorithm.Function import booth_function
# from Algorithm.Population import Population


class Algorithm:
    def __init__(self):
        self.epochs = 1000
        self.Crossover = Crossover('one_point_cross', 0.6)
        self.Population = Population(booth_function, 10, 2, -10, 10, 6)
        self.Mutation = Mutation('one_point_mutation', 0.1)
        self.Inversion = Inversion('standard_inversion', 0.05)
        self.Selection = Selection('best', 1)
        self.EliteStrategy = EliteStrategy(0.1)

    def run(self):
        best_value = []
        avg_value = []
        std_avg_value = []
        best_individual = []

        pop = self.Population.generate_population()
        time_start = time.time()
        for _ in range(self.epochs):
            # dla kazdej eopki
            # ocen polulacje (evaluate)
            fitness = self.Population.evaluate_population(pop)

            #zapisz wartosci do wygenerowania wykresow
            best_value.append(fitness.min())
            avg_value.append(fitness.mean())
            std_avg_value.append(fitness.std())
            index_best = fitness.argsort()[0]
            best_individual.append(self.Population.decode_population(pop)[index_best])

            # zapisz % najlepszych (strategia elitarna)
            elite = self.EliteStrategy.elite(pop, fitness)
            # wybierz gatunki do crossowania (selection)
            # pop, selected_values, not_selected = self.Selection.select(pop, fitness)
            # krzyzowanie gatunków (cross)
            pop = self.Crossover.cross(pop)
            # mutacja i/lub inversja
            pop = self.Mutation.mutate(pop)
            pop = self.Inversion.inverse(pop)
            # mutacja i/lub inversja
            pop = np.concatenate((elite, pop))
        time_execution = time.time() - time_start
        print(f"Algorytm zajął {time_execution:.3f} sekund")

        Plot.draw_save_plot(best_value, 'Wartość funkcji', 'Numer epoki',
                            'Wykres wartości funkcji dla najlepszy osobników', 'best_inidivdual')
        Plot.draw_save_plot(avg_value, 'Wartość funkcji', 'Numer epoki',
                            'Wykres średniej wartości funkcji dla populacji', 'avg_pop')
        Plot.draw_save_plot(std_avg_value, 'Wartość odchylenia standardowego', 'Numer epoki',
                            'Wykres odychlenia standardowego dla populacji', 'avg_std_pop')
        Files.numpy_to_csv(best_individual, 'best_individual.csv')




if __name__ == '__main__':
    Algorithm().run()
