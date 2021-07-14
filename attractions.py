class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute, cuddly critters and crepes"
        self.animals = list()
    
    def add_animal(self, animal):
        self.animals.append(animal)

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "don't get bitten"
        self.animals = list()
    
    def add_animal(self, animal):
        self.animals.append(animal)

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "wetlands and wet bar"
        self.animals = list()
    
    def add_animal(self, animal):
        self.animals.append(animal)