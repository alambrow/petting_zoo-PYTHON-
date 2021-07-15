# import the python datetime module to help us create a timestamp
from datetime import date

class Tadpole:

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False
        self.food = food
        self.__chip_number = chip_num
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, number):
        pass

    def __str__(self):
        return f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}"