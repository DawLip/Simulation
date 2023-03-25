from .entity import Entity


class Food(Entity):
    all = []

    def __init__(self, x: int, y: int, energy):
        super().__init__(x, y)
        self.energy = energy
        Food.all.append(self)

    def eaten(self):
        Food.all.pop(Food.all.index(self))
        Entity.all.pop(Food.all.index(self))

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.energy})"
