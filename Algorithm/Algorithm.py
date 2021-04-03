# from Algorithm.Population import *
from Crossover import *
from Function import booth_function
from Population import *
from Mutation import *
# from Algorithm.Crossover import Crossover
# from Algorithm.Function import booth_function
# from Algorithm.Population import Population


class Algorithm:
    def __init__(self):
        self.Crossover = Crossover('one_point_cross', 0.6)
        self.Population = Population(booth_function, 10, 2, -10, 10, 6)
        self.Mutation = Mutation('one_point_mutation', 0.1)

    def run(self):

        pop = self.Population.generate_population()
        # dla kazdej eopki
        # ocen polulacje (evaluate)
        fitness = self.Population.evaluate_population(pop) # RISES ERROR
        # zapisz % najlepszych (strategia elitarna)
        # wybierz gatunki do crossowania (selection)
        # krzyzowanie gatunków (cross)
        pop = self.Crossover.cross(pop)
        pop = self.Mutation.mutate(pop)
        # mutacja i/lub inversja


if __name__ == '__main__':
    Algorithm().run()
