from movements import Slithering
from animals import Animal

class Butterfly(Animal, Slithering):
        
    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        self.shift = shift
