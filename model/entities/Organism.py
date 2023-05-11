from PIL import Image

from data import data, debug

from .Entity import Entity
from .tmp.TmpFood import TmpFood
from .AdditionalCell import AdditionalCell

# TODO add additional attributes


class Organism(Entity):
    all = []
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
        img=Image.open(r"./resources/img/organism.png"),
    ):
        x2 = x
        y2 = y
        counter = 0
        while not data['CollisionMap'].tryOccupy(x2,y2):
            if counter<data['simWidth']: 
                x2 = (x2+1)%data['simWidth']
            else: 
                counter = 0                       
                y2 = (y2+1)%data['simHeight']
            counter+=1

        super().__init__(x2, y2, img)
        self.energy = energy
        self.buildingPoints = buildingPoints
        self.additionalCells = []  # TODO by default Organizm have NO additionalCells
        self.cooldown = cooldown
        self.parent = parent
        self.children = []
        # always ('what to do', *args)
        self.memory = []

        Organism.all.append(self)

    def delete(self):
        if Organism.all.count(self):
            for additionalCell in self.additionalCells:
                additionalCell.delete()
            Organism.all.remove(self)
            Entity.all.remove(self)
            data["CollisionMap"].freeUpPosition(self.x, self.y)

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
    
    def addAdditionalCell(self):
        additionalCellsPosition=[(additionalCell.relativeX, additionalCell.relativeY) for additionalCell in self.additionalCells]
        
        scope = 1
        scope2 = 1
        i = 2
        numOfCells = len(self.additionalCells) + 1
        while (scope+i)**2 < numOfCells:
            i += 1
            scope += 1

        x = scope
        y = 0
        isLookingForSpace = True
        isNotCross = True
        vertical = True
        while isLookingForSpace:
            if not (x, y) in additionalCellsPosition:
                isLookingForSpace = False
            elif isNotCross:
                if y==0:
                    if x > 0:
                        x = scope * -1
                    else:
                        x = 0
                        y = scope
                else:
                    if y > 0:
                        y = scope * -1
                    else:
                        isNotCross = False
                        x = scope2
                        y = scope
            # else:
            #     if vertical:
            #         if y > 0:
            #             if x > 0:
            #                 x = scope2 * -1
            #             else:
            #                 x = scope2
            #                 y = scope * -1
            #         else:
            #             if x > 0:
            #                 x = scope2 * -1
            #             else:
            #                 vertical = False
            #                 x = scope
            #                 y = scope2
            #     else:
            #         if x > 0:
            #             if y > 0:
            #                 y = scope2 * -1
            #             else:
            #                 x = scope * -1
            #                 y = scope2
            #         else:
            #             pass

        if data['CollisionMap'].tryOccupy(x,y):
            # TODO tmp value
            self.cooldown = 5
            # TODO tmp value
            self.buildingPoints -= 10
            # TODO tmp additionType
            self.additionalCells.append(AdditionalCell(x + self.x, y + self.y, self, None))
        else:
            # TODO tmp additionType
            self.memory.insert(0, ('addAdditionalCell', (x + self.x, y + self.y, None)))

    def move(self, nearestFood, x = None, y = None):
        if self.energy > 1:
            # TODO tmp value
            self.energy -= 1
            # TODO tmp value
            self.cooldown = 1
            nearestFoodX = nearestFood.x - self.x if nearestFood != None else x
            nearestFoodY = nearestFood.y - self.y if nearestFood != None else y
            # check for collision
            wantToGo = [self.x, self.y]
            if abs(nearestFoodX) > abs(nearestFoodY):
                if nearestFoodX > 0:
                    wantToGo[0] += 1
                else:
                    wantToGo[0] -= 1
            else:
                if nearestFoodY > 0:
                    wantToGo[1] += 1
                else:
                    wantToGo[1] -= 1

            isCollision = False
            data['CollisionMap'].freeUpPosition(self.x, self.y)
            for cell in self.additionalCells:
                data['CollisionMap'].freeUpPosition(cell.x, cell.y)

            if data['CollisionMap'].isOccupied(wantToGo[0], wantToGo[1]):
                isCollision = True
            else:
                for cell in self.additionalCells:
                    if data['CollisionMap'].isOccupied(cell.relativeX + wantToGo[0], cell.relativeY + wantToGo[1]):
                        isCollision = True
                        break
            # check for collision
            if isCollision:
                data['CollisionMap'].occupy(self.x, self.y)
                for cell in self.additionalCells:
                    data['CollisionMap'].occupy(cell.x, cell.y)
                if nearestFood != None:
                    self.memory.insert(0, ('waitCollision', nearestFood))
                else:
                    self.memory.insert(0, ('waitCollision', None, nearestFoodX, nearestFoodY))

            else:
                for cell in self.additionalCells:
                    newX = wantToGo[0] + cell.relativeX
                    newY = wantToGo[1] + cell.relativeY
                    data['CollisionMap'].occupy(newX, newY)
                    cell.x = newX
                    cell.y = newY
                                                
                data['CollisionMap'].occupy(wantToGo[0], wantToGo[1]) 
                self.x = wantToGo[0]
                self.y = wantToGo[1]
                if self.memory[0][0] == 'waitCollision':
                    self.memory.pop(0)
                
        else:
            self.delete()

    #  TODO tmp fun
    def division(self):
        self.energy -= self.divisionCost
        # TODO tmp value
        self.cooldown = 5
        newX = self.x - 1
        if self.x < data["simWidth"] / 2:
            newX += 2
        self.children.append(Organism(newX, self.y, self.divisionCost, 0, 20, self))

    def memoryHandler(self):
        match self.memory[0][0]:
            case 'goToFood':
                # TODO tmp solution
                if self.memory[0][1].isExist:
                    if self.memory[0][1].x == self.x and self.memory[0][1].y == self.y:
                        self.eat(self.memory[0][1])
                        self.memory.pop(0)
                    else:
                        self.move(self.memory[0][1])
                else:
                    self.memory.pop(0)

            case 'waitCollision':
                if len(self.memory)>1 and self.memory[1][0] == 'waitCollision':
                    while self.memory[0][0]=='waitCollision':
                        self.memory.pop(0)
                    self.memory.insert(0, ('collision', self.memory.pop(0)[1]))
                else:
                    self.move(self.memory[0][1])

            case 'collision':
                x = self.memory[0][1].x
                y = self.memory[0][1].y
                if self.x > x:
                    if self.y != 0:
                        if data['CollisionMap'].tryOccupy(self.x, self.y-1):
                            self.y -= 1
                            self.memory.pop(0)
                        elif self.x+1 != data['simWidth'] and data['CollisionMap'].tryOccupy(self.x+1, self.y):
                            self.x += 1
                elif self.x < x:
                    if self.y+1 < data['simHeight']:
                        if data['CollisionMap'].tryOccupy(self.x, self.y+1):
                            self.y += 1
                            self.memory.pop(0)
                        elif self.x != 0 and data['CollisionMap'].tryOccupy(self.x-1, self.y):
                            self.x -= 1
                elif self.y > y:
                    if self.x+1 < data['simWidth']:
                        if data['CollisionMap'].tryOccupy(self.x+1, self.y):
                            self.x += 1
                            self.memory.pop(0)
                        elif self.y+1 < data['simHeight'] and data['CollisionMap'].tryOccupy(self.x, self.y+1):
                            self.y += 1
                elif self.x != 0:
                    if data['CollisionMap'].tryOccupy(self.x-1, self.y):
                        self.x -= 1
                        self.memory.pop(0)
                    elif self.y != 0 and data['CollisionMap'].tryOccupy(self.x, self.y-1):
                        self.y -= 1

            case 'addAdditionalCell':
                x = self.memory[0][1][0]
                y = self.memory[0][1][1]
                if x > 0 and x < data['simWidth'] and y > 0 and y < data['simHeight'] and data['CollisionMap'].tryOccupy(x, y):
                    # TODO tmp value
                    self.cooldown = 5
                    # TODO tmp value
                    self.buildingPoints -= 10
                    #                                                      additionType 
                    self.additionalCells.append(AdditionalCell(x, y, self, self.memory[0][1][2]))
                    self.memory.pop(0)
                else:
                    x = self.x*2 - self.memory[0][1][0]
                    y = self.y*2 - self.memory[0][1][1]
                    # !!!only more (or less) not more or equal!!!
                    if x > 0 and x < data['simWidth'] and y > 0 and y < data['simHeight']:
                        self.move(None, x, y)

            case _:
                raise Exception(f"memory's task: {self.memory[0]} not recognized")

    # ------------------------ brain ------------------------
    # TODO AI on IFs
    def brain(self):
        if self.cooldown == 0:
            if len(self.memory) > 0:
                self.memoryHandler()
            else:
                nearestFood = self.lookingForFood()
                if nearestFood != None:
                    if nearestFood.x == self.x and nearestFood.y == self.y:
                        self.eat(nearestFood)
                    # TODO tmp value, remove after "and"
                    elif self.buildingPoints>=10 and len(self.additionalCells)<4:
                        self.addAdditionalCell()
                    # TODO tmp value
                    elif self.energy - self.divisionCost > 200:
                        self.division()
                    else:
                        self.memory.append(('goToFood',nearestFood))
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
        if newValue <= 0:
            self.delete()
        else:
            self.__energy = newValue

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
        assert (
            isinstance(newValue, int) and newValue >= 0
        ), f"cooldown: {self.cooldown}; cooldown must be an int and cooldown >= 0"
        self.__cooldown = newValue

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, newValue):
        assert isinstance(newValue,list) and (len(newValue)==0 or isinstance(newValue[0],(tuple,list))), "memory have to be a list and elements od memory have to be a tuples or lists"
        self.__memory = newValue

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.energy}, {self.buildingPoints}, {self.cooldown}, {self.parent}, {self.img})"
