from movements import Slithering
from animals import Animal

class Insect(Animal, Slithering):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        self.shift = shift
