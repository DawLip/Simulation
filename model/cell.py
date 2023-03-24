from .entity import Entity
from .body import Body


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

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.energy}, {self.buildingPoints})"


# TODO remove
Cell(104, 73, 500, 236)
Cell(104, 73, 500, 236)
