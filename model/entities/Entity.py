from data import data
class Entity:
    all = []

    def __init__(self, x: int, y: int, img: object):
        self.x = x
        self.y = y
        self.img = img
        Entity.all.append(self)
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, newValue: int):
        assert isinstance(newValue, int) and newValue >= 0 and newValue <= data["simWidth"], f"x must be an int and 0 <= x <= {data['simWidth']}"
        self.__x = newValue

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, newValue: int):
        assert isinstance(newValue, int) and newValue >= 0 and newValue <= data["simHeight"], f"y must be an int and 0 <= y <= {data['simHeight']}"
        self.__y = newValue
        
    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, newValue: object):
        # assert newValue.__class__.__name__=='Surface', f'img must be a object like "pygame.image.load(r\'./resources/img/cell.png\')"'
        self.__img = newValue

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.img})"
    def __str__(self):
        return f"{self.__class__.__name__}: x={self.x}, y={self.y}, img={self.img}"
