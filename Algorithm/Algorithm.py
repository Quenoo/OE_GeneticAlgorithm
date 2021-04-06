# from Algorithm.Population import *
from Crossover import *
from Function import booth_function
from Population import *
from Mutation import *
from Inversion import *
from Selection import *
from EliteStrategy import *
# from Algorithm.Crossover import Crossover
# from Algorithm.Function import booth_function
# from Algorithm.Population import Population


class Algorithm:
    def __init__(self):
        self.Crossover = Crossover('one_point_cross', 0.6)
        self.Population = Population(booth_function, 10, 2, -10, 10, 6)
        self.Mutation = Mutation('one_point_mutation', 0.1)
        self.Inversion = Inversion('standard_inversion', 0.05)
        self.Selection = Selection('best', 1)
        self.EliteStrategy = EliteStrategy(0.1)

    def run(self):

        pop = self.Population.generate_population()
        # dla kazdej eopki
        # ocen polulacje (evaluate)
        fitness = self.Population.evaluate_population(pop)
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


if __name__ == '__main__':
    Algorithm().run()
