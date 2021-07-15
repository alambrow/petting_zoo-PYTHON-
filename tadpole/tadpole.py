from animals import Animal

class Tadpole(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.swimming = True
        self.slithering = False
        self.walking = False