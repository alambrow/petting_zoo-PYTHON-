from datetime import date

class Newt:
    
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

