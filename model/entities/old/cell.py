from ..Entity import Entity
from .body import Body
from .food import Food


class Cell(Entity):
    all = []

    def __init__(self, x: int, y: int, energy: int, buildingPoints: int):
        super().__init__(x, y)
        assert (
            isinstance(energy, (int, float)) and energy > 0
        ), "energy must be a num and energy > 0"
        assert isinstance(buildingPoints, (int, float)), "buildingPoints must be a num"

        self.__energy = energy
        self.buildingPoints = buildingPoints
        Cell.all.append(self)

    def death(self):
        Cell.all.pop(Cell.all.index(self))
        Entity.all.pop(Entity.all.index(self))
        Body(self.x, self.y)

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, newEnergy):
        assert isinstance(newEnergy, (int, float)), "energy must be a num"
        if newEnergy <= 0:
            self.death()
        else:
            self.__energy = newEnergy

    def lookingForFood(self):
        nearestFood = None
        minDistance = None
        for food in Food.all:
            # TODO tmp distance counting
            distance = (self.x - food.x) ** 2 + (self.y - food.y) ** 2
            if minDistance == None or minDistance > distance:
                minDistance = distance
                nearestFood = food

        return nearestFood

    def eat(self, food):
        self.energy += food.energy
        food.eaten()

    def move(self):
        nearestFood = self.lookingForFood()
        if nearestFood != None:
            self.energy -= 1
            distanceX = nearestFood.x - self.x
            distanceY = nearestFood.y - self.y
            if abs(distanceX) or abs(distanceY) <= 1:
                self.eat(nearestFood)
            if abs(distanceX) > abs(distanceY):
                if distanceX > 0:
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if distanceY > 0:
                    self.y += 1
                else:
                    self.y -= 1

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.energy}, {self.buildingPoints})"
