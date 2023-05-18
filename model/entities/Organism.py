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
        # else:
        #     # TODO tmp additionType
        #     self.memory.insert(0, ('addAdditionalCell', (x + self.x, y + self.y, None)))
            
    def physicalMove(self, wantToGoX: int, wantToGoY: int):
        self.x = wantToGoX
        self.y = wantToGoY
        for cell in self.additionalCells:
            cell.x = wantToGoX + cell.relativeX
            cell.y = wantToGoY + cell.relativeY
    
    def logicalMove(self, wantToGoX: int, wantToGoY: int) -> bool:
        if wantToGoX < 0 or wantToGoY < 0 or wantToGoX > data['simWidth'] or wantToGoY > data['simHeight']:   
            return False
        for cell in self.additionalCells:
            if wantToGoX+cell.relativeX < 0 or wantToGoY+cell.relativeY < 0 or wantToGoX+cell.relativeX > data['simWidth'] or wantToGoY+cell.relativeY > data['simHeight']:   
                return False
            
        data['CollisionMap'].freeUpPosition(self.x, self.y)
        for cell in self.additionalCells:
            data['CollisionMap'].freeUpPosition(cell.x, cell.y)

        isCollision = False
        if data['CollisionMap'].isOccupied(wantToGoX, wantToGoY):
            isCollision = True
        else:
            for cell in self.additionalCells:
                if data['CollisionMap'].isOccupied(cell.relativeX + wantToGoX, cell.relativeY + wantToGoY):
                    isCollision = True
                    break
                
        if isCollision:
            data['CollisionMap'].occupy(self.x, self.y)
            for cell in self.additionalCells:
                data['CollisionMap'].occupy(cell.x, cell.y)
            return False
        else:
            data['CollisionMap'].occupy(wantToGoX, wantToGoY)
            for cell in self.additionalCells:
                data['CollisionMap'].occupy(cell.relativeX + wantToGoX, cell.relativeY + wantToGoY)
            return True
                
    def move(self, x: int, y: int):
        if self.energy > 1:
            # TODO tmp value
            self.energy -= 1
            # TODO tmp value
            self.cooldown = 1
            
            distanceX = x - self.x
            distanceY = y - self.y
            wantToGoX = self.x
            wantToGoY = self.y
            if abs(distanceX) > abs(distanceY):
                if distanceX > 0: wantToGoX += 1
                else:             wantToGoX -= 1
            else:
                if distanceY > 0: wantToGoY += 1
                else:             wantToGoY -= 1
                
            if self.logicalMove(wantToGoX, wantToGoY):
                self.physicalMove(wantToGoX, wantToGoY)
            else:
                self.memory.insert(0, ('waitCollision', (wantToGoX, wantToGoY)))
                 
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
        task = self.memory[0]
        match task[0]:
            case 'goToFood':
                # TODO tmp solution
                if task[1].isExist:
                    if task[1].x == self.x and task[1].y == self.y:
                        self.eat(task[1])
                        self.memory.pop(0)
                    else:
                        self.move(task[1].x, task[1].y)
                else:
                    self.memory.pop(0)

            case 'waitCollision':
                self.memory.pop(0)
                wantToGoX = task[1][0]
                wantToGoY = task[1][1]
                if self.logicalMove(wantToGoX, wantToGoY):
                    self.physicalMove(wantToGoX, wantToGoY)
                else:
                    self.memory.insert(0, ('collision', (wantToGoX, wantToGoY)))           

            case 'collision':
                wantToGoX = task[1][0]
                wantToGoY = task[1][1]
                if self.x > wantToGoX:
                    if self.logicalMove(wantToGoX, wantToGoY-1):
                        self.physicalMove(wantToGoX, wantToGoY-1)
                        self.memory.pop(0)
                    else: 
                        if min([self.y, *[cell.y for cell in self.additionalCells]]):
                            if self.logicalMove(wantToGoX+1, wantToGoY):
                                self.physicalMove(wantToGoX+1, wantToGoY)
                        else: self.memory.pop(0)
                        
                elif self.x < wantToGoX:
                    if self.logicalMove(wantToGoX, wantToGoY+1):
                        self.physicalMove(wantToGoX, wantToGoY+1)
                        self.memory.pop(0)
                    else: 
                        if max([self.y, *[cell.y for cell in self.additionalCells]]) != data['simHeight']:
                            if self.logicalMove(wantToGoX-1, wantToGoY):
                                self.physicalMove(wantToGoX-1, wantToGoY)
                        else: self.memory.pop(0)
                        
                elif self.y > wantToGoY:
                    if self.logicalMove(wantToGoX+1, wantToGoY):
                        self.physicalMove(wantToGoX+1, wantToGoY)
                        self.memory.pop(0)
                    else: 
                        if min([self.x, *[cell.x for cell in self.additionalCells]]):
                            if self.logicalMove(wantToGoX, wantToGoY+1):
                                self.physicalMove(wantToGoX, wantToGoY+1)
                        else: self.memory.pop(0)
                         
                else:
                    if self.logicalMove(wantToGoX-1, wantToGoY):
                        self.physicalMove(wantToGoX-1, wantToGoY)
                        self.memory.pop(0)
                    else: 
                        if max([self.x, *[cell.x for cell in self.additionalCells]]) != data['simWidth']:
                            if self.logicalMove(wantToGoX, wantToGoY-1):
                                self.physicalMove(wantToGoX, wantToGoY-1)
                        else: self.memory.pop(0)

            # case 'addAdditionalCell':
            #     x = self.memory[0][1][0]
            #     y = self.memory[0][1][1]
            #     if x > 0 and x < data['simWidth'] and y > 0 and y < data['simHeight'] and data['CollisionMap'].tryOccupy(x, y):
            #         # TODO tmp value
            #         self.cooldown = 5
            #         # TODO tmp value
            #         self.buildingPoints -= 10
            #         #                                                      additionType 
            #         self.additionalCells.append(AdditionalCell(x, y, self, self.memory[0][1][2]))
            #         self.memory.pop(0)
            #     else:
            #         x = self.x*2 - self.memory[0][1][0]
            #         y = self.y*2 - self.memory[0][1][1]
            #         # !!!only more (or less) not more or equal!!!
            #         if x > 0 and x < data['simWidth'] and y > 0 and y < data['simHeight']:
            #             self.move(None, x, y)

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
                    # if nearestFood.x == self.x and nearestFood.y == self.y:
                    #     self.eat(nearestFood)
                    # TODO tmp value, remove after "and"
                    if self.buildingPoints>=10 and len(self.additionalCells)<4:
                        self.addAdditionalCell()
                    # TODO tmp value
                    elif self.energy - self.divisionCost > 200:
                        self.division()
                    else:
                        self.memory.append(('goToFood',nearestFood))
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
