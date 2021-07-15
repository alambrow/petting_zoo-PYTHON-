from movements import Walking, Swimming
from animals import Animal

class Frog(Animal, Walking, Swimming):
    
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        Swimming.__init__(self)
        Walking.__init__(self)
