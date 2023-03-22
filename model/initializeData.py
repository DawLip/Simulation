from random import randrange

from data import data, GUI, entities

class Cell:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Food:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    
def initializeData():
    for _ in range(data['initialCellNumber']):
        tmp = Cell(randrange(data['simWidth']-1),randrange(data['simHeight']-1))
        entities['cells'].append(tmp)
    
    for _ in range(data['initialFoodNumber']):
        tmp = Food(randrange(data['simWidth']-1),randrange(data['simHeight']-1))
        entities['food'].append(tmp)