from Algorithm.Population import *
from Algorithm.Crossover import *
from Algorithm.Function import booth_function


class Algorithm:
    def __init__(self):
        self.Crossover = Crossover('one_point_cross', 0.6)
        self.Population = Population(booth_function, 10, 2, -10, 10, 6)

    def run(self):

        pop = self.Population.generate_population()

        # dla kazdej eopki
        # ocen polulacje (evaluate)
        # zapisz % najlepszych (strategia elitarna)
        # wybierz gatunki do crossowania (selection)
        # krzyzowanie gatunków (cross)
        #pop = self.Crossover.cross(pop)
        # mutacja i/lub inversja
