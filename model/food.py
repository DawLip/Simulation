from .entity import Entity

class Food(Entity):
    all=[]
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        Food.all.append(self)
        # assert isinstance(energy,(int,float)) and energy>0, 