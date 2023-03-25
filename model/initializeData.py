from random import randrange

from data import data, GUI
from .food import Food
from .cell import Cell


def initializeData():
    for _ in range(data["initialCellNumber"]):
        # TODO default values
        Cell(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), 10, 50)

        # TODO default values
    for _ in range(data["initialFoodNumber"]):
        Food(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1), 50)
