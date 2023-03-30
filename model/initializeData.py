from random import randrange

from .entities.entities import Food, Cell

from data import data


def initializeData():
    for _ in range(data["initialCellNumber"]):
        # TODO default values
        Cell(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), 10, 50)

        # TODO default values
    for _ in range(data["initialFoodNumber"]):
        Food(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), 50)
