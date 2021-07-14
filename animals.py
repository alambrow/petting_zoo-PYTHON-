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

b_fly = Butterfly("b_fly", "monarch", "morning")
theodor = Tadpole("theodor", "young one", "morning")
bby_fuzz = Donkey("Baby Fuzz", "Gray one", "morning")
al = Eel("al", "electric eel", "afternoon")
piscus = Fish("Piscus", "Goldfish", "afternoon")
mr_wartz = Frog("Mr Wartz", "Green one", "afternoon")
llt_fuzz = Goat("Little Fuzz", "Spotted", "afternoon")
buzz = Insect("buzz", "bee", "afternoon")
mrs_Fuzz = Llama("Mrs. Fuzz", "shaggy one", "evening")
sam = Newt("sam", "yellow one", "evening")
littleP = Pony("Little Pony", "Shetland", "evening")
sal = Salamander("sal", "green one", "evening")
hry_bear = Sheep("Hairy Bear", "Brown sheep", "evening")
slytherz = Snake("slytherz", "rattler", "evening")
mr_T = Toad("Mr T", "warty", "evening")

print(f"{b_fly.name}, the {b_fly.species}, is available to pet during the {b_fly.shift} shift")