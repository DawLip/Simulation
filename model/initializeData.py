from random import randrange, seed

from .entities.importEntities import Organism
from .entities.tmp.TmpFood import TmpFood

# from .environment.OrganicMatter import OrganicMatter
from .environment.CollisionMap import CollisionMap

from data import data

# randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1),


def initializeData():
    seed(data['seed'])
    
    # data['OrganicMatter']=OrganicMatter()
    data["CollisionMap"] = CollisionMap()
    # TODO tmp init
    for _ in range(data["initialFoodNumber"]):
        TmpFood(randrange(1, data["simWidth"] - 1), randrange(1, data["simHeight"] - 1))
        
    for _ in range(data["initialCellNumber"]):
        # TODO default values
        Organism(randrange(1, data["simWidth"] - 1), randrange(1, data["simHeight"] - 1), 100, randrange(5)*10)
