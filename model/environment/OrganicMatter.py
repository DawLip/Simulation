from data import data

from .MapConstructor import MapConstructor
class OrganicMatter(MapConstructor):
    def __init__(self, map=[[i for i in range(data['simWidth'])] for _ in range(data['simHeight'])]):
        assert isinstance(map, list) and len(map)==data['simHeight'] and len(map[0])==data['simWidth'], "map must be a list and height == data['simHeight'] and width==data['simWidth']"
        super().__init__(map)        
