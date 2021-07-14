from datetime import date

class Goat:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True

