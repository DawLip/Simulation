from data import data


class Entity:
    all = []

    def __init__(self, x: int, y: int):
        assert (
            isinstance(x, int) and x >= 0 and x <= data["simWidth"]
        ), f"x must be an int and 0 <= x <= {data['simWidth']}"
        assert (
            isinstance(y, int) and y >= 0 and y <= data["simHeight"]
        ), f"y must be an int and 0 <= y <= {data['simHeight']}"

        self.__x = x
        self.__y = y
        Entity.all.append(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, newX: int):
        assert (
            isinstance(newX, int) and newX >= 0 and newX <= data["simWidth"]
        ), f"x must be an int and 0 <= x <= {data['simWidth']}"
        self.__x = newX

    @y.setter
    def y(self, newY: int):
        assert (
            isinstance(newY, int) and newY >= 0 and newY <= data["simHeight"]
        ), f"y must be an int and 0 <= y <= {data['simHeight']}"
        self.__y = newY

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"
