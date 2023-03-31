from random import randrange
from pygame import image

from .entities.importEntities import Organism

from data import data


def initializeData():
    for _ in range(data["initialCellNumber"]):
        # TODO default values
        # pygame.image.load(r'./resources/img/cell.png')  
        Organism(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), image.load(r'./resources/img/organism.png'),10,10,0)
