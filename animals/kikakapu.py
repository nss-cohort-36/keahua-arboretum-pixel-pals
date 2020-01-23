from animals import Animal
from interfaces import IFreshwater
from interfaces import Identifiable
class Kīkākapu(Animal, IFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Planktonic Animals", "Vegetation" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Kīkākapu ate {prey} for a meal")
        else:
            print(f"The Kīkākapu rejects the {prey}")


    def __str__(self):
        return f"Kīkākapu {self.id}. I want more Planktonic Animals but...... Crunchberries will do!"