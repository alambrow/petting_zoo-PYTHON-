# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True

mrs_Fuzz = Llama("Mrs. Fuzz", "shaggy one")
print(mrs_Fuzz.name)

class Donkey:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True

bby_fuzz = Donkey("Baby Fuzz", "Gray one")

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

llt_fuzz = Goat("Little Fuzz", "Spotted")

class Pony:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True

littleP = Pony("Little Pony", "Shetland")

class Sheep:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True

hry_bear = Sheep("Hairy Bear", "Brown sheep")

class Frog:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

mr_wartz = Frog("Mr Wartz", "Green one")

class Fish:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

piscus = Fish("Piscus", "Goldfish")

class Toad:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

mr_T = Toad("Mr T", "warty")

class Newt:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

sam = Newt("sam", "yellow one")

class Eel:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False

al = Eel("al", "electric eel")

class Snake:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False

slytherz = Snake("slytherz", "rattler")

class Salamander:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False

sal = Salamander("sal", "green one")

class Insect:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False

buzz = Insect("buzz", "bee")

class Butterfly:
        
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False

b_fly = Butterfly("b_fly", "monarch")

class Tadpole:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False

theodor = Tadpole("theodor", "young one")
print(theodor.name)