from animals import Animal
from movements import Swimming

class Fish(Animal, Swimming):
    
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        Swimming.__init__(self)

