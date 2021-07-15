from animals import Animal

class Butterfly(Animal):
        
    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.swimming = False
        self.slithering = True
        self.walking = False