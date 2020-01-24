# from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome
# from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable, Biome):

    def __init__(self, name):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        # try:
        #     if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        # except AttributeError:
        #     raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")
        #     input("> Press any key to continue ")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
