from pygame import image
from data import data

from .Entity import Entity
from .tmp.Tmp_food import TmpFood

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
        actions: int,
        buildingPoints: int,
        parent: object = None,
        img = image.load(r'./resources/img/organism.png'),
        ):
        super().__init__(x, y, img)
        self.energy = energy
        self.buildingPoints = buildingPoints
        self.__additionalCells = [] #TODO by default Organizm have NO additionalCells
        self.actions = actions
        self.__actionsLeft = actions
        self.__parent = parent
        self.__children = []
        
        # place for additional attributes
        
        Organism.all.append(self)
        
    def delete(self):
        Entity.all.pop(Entity.all.index(self))
        Organism.all.pop(Organism.all.index(self))
        
    def eat(self, nearestFood):
        self.energy += nearestFood.energy
        nearestFood.delete()
        
    # TODO change looking for tmp foo to organic materia
    def lookingForFood(self):
        nearestFood = None
        minDistance = None
        for food in TmpFood.all:
            distance = abs(self.x - food.x) + abs(self.y - food.y) 
            if minDistance == None or minDistance > distance:
                minDistance = distance
                nearestFood = food
        return nearestFood
    
    def move(self):
        nearestFood = self.lookingForFood()
        if nearestFood != None:
            self.energy = self.energy - 1
            nearestFoodX = nearestFood.x - self.x 
            nearestFoodY = nearestFood.y - self.y
            if abs(nearestFoodX) > abs(nearestFoodY):
                if nearestFoodX > 0: self.x += 1
                else:                self.x -= 1
            else:
                if nearestFoodY > 0:    self.y += 1
                elif nearestFoodY != 0: self.y -= 1
            if abs(nearestFoodX) == 0 and abs(nearestFoodY) == 0:
                self.eat(nearestFood)

    #  TODO tmp fun
    def division(self):
        if self.energy > self.divisionCost:
            self.energy = self.energy - self.divisionCost
            newX = self.x-1
            if self.x < data['simWidth']/2:
                newX+=2
            self.children.append(Organism(newX, self.y, self.divisionCost, self.actions, 0, self))
        
        
    @property
    def energy(self):
        return self.__energy
    @energy.setter
    def energy(self, newValue: int):
        assert isinstance(newValue, int), "energy must be an int"
        if newValue <= 0: self.delete()
        else: self.__energy = newValue
        # TODO tmp division
        if newValue > 150:
            self.division()
    
    @property
    def buildingPoints(self):
        return self.__buildingPoints
    @buildingPoints.setter
    def buildingPoints(self, newValue: int):
        assert isinstance(newValue, int), "buildingPoints must be an int"
        self.__buildingPoints = newValue
    
    # TODO additionalCells have NOT setter 
    @property
    def additionalCells(self):
        return self.__additionalCells
    # @additionalCells.setter
    # def additionalCells(self, newValue: list):
    #     assert isinstance(newValue, list), "additionalCells must be an list"
    #     self.__additionalCells = newValue
    
    # TODO parent have NOT setter 
    @property
    def parent(self):
        return self.__parent
    # @parent.setter
    # def parent(self, newValue: object):
    #     assert isinstance(newValue, object), "parent must be an object"
    #     self.__parent = newValue
    
    # TODO children have NOT setter 
    @property
    def children(self):
        return self.__children
    # @children.setter
    # def children(self, newValue: list):
    #     assert isinstance(newValue, list), "children must be an list"
    #     self.__children = newValue
    
    @property
    def actions(self):
        return self.__actions
    @actions.setter
    def actions(self, newValue: int):
        assert isinstance(newValue, int), "actions must be an int"
        self.__actions = newValue
    
    # TODO actionsLeft have NOT setter 
    @property
    def actionsLeft(self):
        return self.__actionsLeft
    # @actionsLeft.setter
    # def actionsLeft(self, newValue: int):
    #     assert isinstance(newValue, int), "actionsLeft must be an int"
    #     self.__actionsLeft = newValue
    