from movements import Walking
from animals import Animal

class Sheep(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift
        Walking.__init__(self)