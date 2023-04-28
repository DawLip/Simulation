from data import data

from .MapConstructor import MapConstructor

class CollisionMap(MapConstructor):
    def __init__(self, map = [[False for _ in range(data['simWidth'])] for _ in range(data['simHeight'])]):
        super().__init__(map)
        assert isinstance(map, list) and len(map)==data['simHeight'] and len(map[0])==data['simWidth'], "map must be a list and height == data['simHeight'] and width==data['simWidth']"
        self.map = map

    def isOccupied(self, x, y):
        return self.map[y][x]
    
    def freeUpPosition(self, x, y):
        self.map[y][x] = False

    def tryOccupy(self, x, y):
        if self.map[y][x]:
            return False
        self.map[y][x] = True
        return True
        