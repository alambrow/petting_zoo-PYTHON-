from attractions import PettingZoo, SnakePit, Wetlands
from butterfly import Butterfly
from tadpole import Tadpole
from donkey import Donkey
from eel import Eel
from fish import Fish
from frog import Frog
from goat import Goat
from insect import Insect
from llama import Llama
from newt import Newt
from pony import Pony
from salamander import Salamander
from sheep import Sheep
from snake import Snake
from toad import Toad

b_fly = Butterfly("b_fly", "monarch", "morning", "sugar", 123)
theodor = Tadpole("theodor", "young one", "morning", "leaves", 456)
bby_fuzz = Donkey("Baby Fuzz", "Gray one", "morning", "grass", 789)
al = Eel("al", "electric eel", "afternoon", "seaweed", 109)
piscus = Fish("Piscus", "Goldfish", "afternoon", "seaweed", 101)
mr_wartz = Frog("Mr Wartz", "Green one", "afternoon", "flies", 102)
llt_fuzz = Goat("Little Fuzz", "Spotted", "afternoon", "barley", 103)
buzz = Insect("buzz", "bee", "afternoon", "pollen", 104)
mrs_Fuzz = Llama("Mrs. Fuzz", "shaggy one", "evening", "barley", 144)
sam = Newt("sam", "yellow one", "evening", "flies", 145)
littleP = Pony("Little Pony", "Shetland", "evening", "hay", 146)
sal = Salamander("sal", "green one", "evening", "insects", 147)
hry_bear = Sheep("Hairy Bear", "Brown sheep", "evening", "grass", 148)
slytherz = Snake("slytherz", "rattler", "evening", "people", 149)
mr_T = Toad("Mr T", "warty", "evening", "flies", 150)

varmint_village = PettingZoo("Varmint Village")
varmint_village.add_animal(buzz)
varmint_village.add_animal(b_fly)

slither_inn = SnakePit("Slither Inn")
slither_inn.add_animal(slytherz)
slither_inn.add_animal(bby_fuzz)

critter_cove = Wetlands("Critter Cove")
critter_cove.add_animal(mr_T)
critter_cove.add_animal(al)
critter_cove.add_animal(piscus)

for animal in varmint_village.animals:
    print(f'You can find {animal.name}, the {animal.species} (chip_num: {animal.chip_number}), in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name}, the {animal.species} (chip_num: {animal.chip_number}), in {slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name}, the {animal.species} (chip_num: {animal.chip_number}), in {critter_cove.attraction_name}')

# Why is this throwing 'None'?
print(mr_wartz.feed())