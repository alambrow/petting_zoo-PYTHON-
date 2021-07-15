class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self.animals)} animals)'

    def __len__(self):
        return len(self.animals)
    
    @property
    def last_critter_added(self):
        return self.animals[-1]

class PettingZoo(Attraction):
    def __init__(self, name, description="cute, cuddly critters and crepes"):
        super().__init__(name, description)
    

class SnakePit(Attraction):
    def __init__(self, name, description="don't get bitten"):
        super().__init__(name, description)

class Wetlands(Attraction):
    def __init__(self, name, description="wetlands and wet bar"):
        super().__init__(name, description)