from attractions import PettingZoo, SnakePit, Wetlands
from animals import buzz, slytherz, mr_T, b_fly, bby_fuzz, al, piscus

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
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')