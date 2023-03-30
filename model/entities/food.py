from .entity import Entity


class Food(Entity):
    all = []
# test
    def __init__(self, x: int, y: int, energy):
        super().__init__(x, y)
        assert (
            isinstance(energy, (int, float)) and energy > 0
        ), "energy must be a num and energy > 0"
        self.__energy = energy
        Food.all.append(self)

    def eaten(self):
        Food.all.pop(Food.all.index(self))
        Entity.all.pop(Food.all.index(self))

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, newEnergy):
        assert isinstance(newEnergy, (int, float)), "energy must be a num"
        if newEnergy <= 0:
            self.eaten()
        else:
            self.__energy = newEnergy

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.energy})"
