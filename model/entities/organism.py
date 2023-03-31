from pygame import image
from data import data

from .entity import Entity

# TODO add additional attributes
class Organism(Entity):
    all=[]
    # TODO tmp value - divisionCost
    divisionCost = 50
    def __init__(
        self,
        x: int,
        y: int,
        img: object,
        energy: int,
        actions: int,
        buildingPoints: int,
        parent: object = None,
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
    
    #  TODO tmp fun
    def division(self):
        if self.energy > self.divisionCost:
            self.energy = self.energy - self.divisionCost
            newX = self.x-1
            if self.x < data['simWidth']/2:
                newX+=2
            self.children.append(Organism(newX, self.y, image.load(r'./resources/img/organism.png'), self.divisionCost, self.actions, 0, self))
        
        
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
    