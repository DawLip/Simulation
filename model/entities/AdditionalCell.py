from PIL import Image

from .Entity import Entity

from data import data

class AdditionalCell(Entity):
    all=[]
    # TODO tmp
    additionTypes={None, 'foto', 'sth'}

    def __init__(
        self, 
        x: int, 
        y: int,
        mainCell: object, 
        additionType: str, 
        lvl: int = 1, 
        # TODO change to proper value
        img: object = Image.open(r"./resources/img/organism.png")
    ):
        super().__init__(x, y, img)
        self.mainCell = mainCell
        self.additionType = additionType
        self.lvl = lvl
        self.relativeX = self.x - mainCell.x
        self.relativeY = self.y - mainCell.y

        # CollisionMap is handled in Organism.py
        AdditionalCell.all.append(self)

    def delete(self):
        AdditionalCell.all.pop(AdditionalCell.all.index(self))
        Entity.all.pop(Entity.all.index(self))
        data["CollisionMap"].freeUpPosition(self.x, self.y)


    @property
    def mainCell(self):
        return self.__mainCell
    @mainCell.setter
    def mainCell(self, newValue):
        self.__mainCell = newValue
        
    @property
    def additionType(self):
        return self.__additionType
    @additionType.setter
    def additionType(self, newValue):
        assert newValue in self.additionTypes, f"additionType: {newValue} is not recognized."
        self.__additionType = newValue

    @property
    def lvl(self):
        return self.__lvl
    @lvl.setter
    def lvl(self, newValue):
        assert isinstance(newValue, int) and newValue > 0, f"lvl must be an int and lvl > 0."
        self.__lvl = newValue

    @property
    def relativeX(self):
        return self.__relativeX
    @relativeX.setter
    def relativeX(self, newValue):
        assert isinstance(newValue, int), f"relativeX must be an int."
        self.__relativeX = newValue

    @property
    def relativeY(self):
        return self.__relativeY
    @relativeY.setter
    def relativeY(self, newValue):
        assert isinstance(newValue, int), f"relativeY must be an int."
        self.__relativeY = newValue

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.mainCell}, {self.additionType},  {self.lvl},  {self.img})"
    