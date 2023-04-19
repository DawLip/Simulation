from pygame import image

from ..Entity import Entity

class TmpFood(Entity):
    all = []
    def __init__(self, x: int, y: int, img = image.load(r'./resources/img/food.png')):
        super().__init__(x, y, img)
        self.energy = 50
        
        TmpFood.all.append(self)
        
    def delete(self):
        TmpFood.all.pop(TmpFood.all.index(self))
        Entity.all.pop(Entity.all.index(self))
        
    def __repr__(self): 
        return f"{super().__repr__()[:-1]}, {self.energy})"
    