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

b_fly = Butterfly("b_fly", "monarch", "morning", "sugar")
theodor = Tadpole("theodor", "young one", "morning", "leaves")
bby_fuzz = Donkey("Baby Fuzz", "Gray one", "morning", "grass")
al = Eel("al", "electric eel", "afternoon", "seaweed")
piscus = Fish("Piscus", "Goldfish", "afternoon", "seaweed")
mr_wartz = Frog("Mr Wartz", "Green one", "afternoon", "flies")
llt_fuzz = Goat("Little Fuzz", "Spotted", "afternoon", "barley")
buzz = Insect("buzz", "bee", "afternoon", "pollen")
mrs_Fuzz = Llama("Mrs. Fuzz", "shaggy one", "evening", "barley")
sam = Newt("sam", "yellow one", "evening", "flies")
littleP = Pony("Little Pony", "Shetland", "evening", "hay")
sal = Salamander("sal", "green one", "evening", "insects")
hry_bear = Sheep("Hairy Bear", "Brown sheep", "evening", "grass")
slytherz = Snake("slytherz", "rattler", "evening", "people")
mr_T = Toad("Mr T", "warty", "evening", "flies")

print(f"{b_fly.name}, the {b_fly.species}, is available to pet during the {b_fly.shift} shift.")
print(b_fly.feed())

print(mr_T.feed())