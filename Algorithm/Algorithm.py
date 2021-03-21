from Algorithm.Population import *
from Algorithm.Function import booth_function


class Algorithm:
    def run(self):
        pop = Population(booth_function, 10, 2, -10, 10, 6)

        # dla kazdej eopki
        # ocen polulacje (evaluate)
        # zapisz % najlepszych (strategia elitarna)
        # wybierz gatunki do crossowania (selection)
        # krzyzowanie gatunków (cross)
        # mutacja i/lub inversja
