from pygame import image

from .Entity import Entity

class AdditionalCell(Entity):
    def __init__(self, x: int, y: int, additionType: str, lvl: int = 1, img: object = image.load(r'./resources/img/organism.png')):
        super().__init__(x, y, img)
        self.additionType = additionType
        self.lvl = lvl
        