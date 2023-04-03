from random import randrange

from .entities.importEntities import Organism
from .entities.tmp.Tmp_food import TmpFood

from .environment.OrganicMatter import OrganicMatter

from data import data

# randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1),

def initializeData():
    OrganicMatter()
    # TODO tmp init
    for _ in range(data['initialFoodNumber']):
        TmpFood(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1))
    
    for _ in range(data["initialCellNumber"]):
        # TODO default values
        # pygame.image.load(r'./resources/img/cell.png')  
        Organism(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), 100, 10, 0)
