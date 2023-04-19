from pygame import image
from data import data

from .Entity import Entity
from .tmp.TmpFood import TmpFood
# TODO add additional attributes
class Organism(Entity):
    all=[]
    # TODO tmp value - divisionCost
    divisionCost = 50
    def __init__(
        self,
        x: int,
        y: int,
        energy: int,
        buildingPoints: int,
        cooldown: int = 0,
        parent: object = None,
        img = image.load(r'./resources/img/organism.png'),
        ):
        super().__init__(x, y, img)
        self.energy = energy
        self.buildingPoints = buildingPoints
        self.additionalCells = [] #TODO by default Organizm have NO additionalCells
        self.cooldown = cooldown
        self.parent = parent
        self.children = []
        
        # place for additional attributes
        
        Organism.all.append(self)
        
    def delete(self):
        if Organism.all.count(self):
            Organism.all.pop(Organism.all.index(self))
            Entity.all.pop(Entity.all.index(self))
        
    def eat(self, nearestFood):
        # TODO tmp value
        self.energy += nearestFood.energy
        nearestFood.delete()
        # TODO tmp value
        self.cooldown = 3
        
    # TODO change looking for tmp foo to organic matter
    def lookingForFood(self):
        nearestFood = None
        minDistance = None
        for food in TmpFood.all:
            distance = abs(self.x - food.x) + abs(self.y - food.y) 
            if minDistance == None or minDistance > distance:
                minDistance = distance
                nearestFood = food
        return nearestFood
    
    def move(self, nearestFood):
        # TODO tmp value
        self.energy -= 1
        # TODO tmp value
        self.cooldown = 1
        nearestFoodX = nearestFood.x - self.x 
        nearestFoodY = nearestFood.y - self.y
        if abs(nearestFoodX) > abs(nearestFoodY):
            if nearestFoodX > 0: self.x += 1
            else:                self.x -= 1
        else:
            if nearestFoodY > 0: self.y += 1
            # TODO check
            else:                self.y -= 1
            # elif nearestFoodY != 0: self.y -= 1
        
    #  TODO tmp fun
    def division(self):
        self.energy -= self.divisionCost 
        # TODO tmp value
        self.cooldown = 5
        newX = self.x-1
        if self.x < data['simWidth']/2:
            newX+=2
        self.children.append(Organism(newX, self.y, self.divisionCost, 0, 20, self))
    
# ------------------------ brain ------------------------
    # TODO AI on IFs
    def brain(self):
        if self.cooldown == 0:
            nearestFood = self.lookingForFood()
            if nearestFood != None:
                if nearestFood.x == self.x and nearestFood.y == self.y: 
                    self.eat(nearestFood)
                # TODO tmp value
                elif self.energy - self.divisionCost > 150:
                    self.division()                    
                else: 
                    self.move(nearestFood)
        else:
            self.cooldown -= 1
        
        # TODO tmp value
        self.energy -= 1
# ------------------------ brain ------------------------
        
    @property
    def energy(self):
        return self.__energy
    @energy.setter
    def energy(self, newValue: int):
        assert isinstance(newValue, int), "energy must be an int"
        if newValue <= 0: self.delete()
        else: self.__energy = newValue
    
    @property
    def buildingPoints(self):
        return self.__buildingPoints
    @buildingPoints.setter
    def buildingPoints(self, newValue: int):
        assert isinstance(newValue, int), "buildingPoints must be an int"
        self.__buildingPoints = newValue
    
    @property
    def additionalCells(self):
        return self.__additionalCells
    @additionalCells.setter
    def additionalCells(self, newValue: list):
        assert isinstance(newValue, list), "additionalCells must be an list"
        self.__additionalCells = newValue
    
    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, newValue: object):
        assert isinstance(newValue, (object, None)), "parent must be an object or None"
        self.__parent = newValue
    
    @property
    def children(self):
        return self.__children
    @children.setter
    def children(self, newValue: list):
        assert isinstance(newValue, list), "children must be an list"
        self.__children = newValue
    
    @property
    def cooldown(self):
        return self.__cooldown
    @cooldown.setter
    def cooldown(self, newValue: int):
        assert isinstance(newValue, int) and newValue >= 0, f'cooldown: {self.cooldown}; cooldown must be an int and cooldown >= 0'
        self.__cooldown = newValue
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.energy}, {self.buildingPoints}, {self.cooldown}, {self.parent}, {self.img})"
