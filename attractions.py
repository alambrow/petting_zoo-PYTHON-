from movements import Swimming, Walking


class Attraction:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()
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
    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')
    

class SnakePit(Attraction):
    def __init__(self, name, description="don't get bitten"):
        super().__init__(name, description)
    def add_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

class Wetlands(Attraction):
    def __init__(self, name, description="wetlands and wet bar"):
        super().__init__(name, description)
    def add_animal(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal.name} now lives in {self.attraction_name}")
        else:
            print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')