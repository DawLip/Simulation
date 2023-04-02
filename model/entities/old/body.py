from ..Entity import Entity

class Body(Entity):
    all = []

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
