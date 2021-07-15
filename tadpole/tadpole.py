from movements import Swimming
from animals import Animal

class Tadpole(Animal, Swimming):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift
        Swimming.__init__(self)