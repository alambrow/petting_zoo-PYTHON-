from datetime import date

class Frog:
    
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food
    
    def __str__(self):
        return f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}"
