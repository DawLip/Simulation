class MapConstructor:
    def __init__(self, map=[[]]):
        assert isinstance(map, list), "map must be a list"
        self.map = map
        
    def __str__(self):
        string = ''
        
        # only for printing "CollisionMap"
        matrix = self.map
        if self.__class__.__name__ == 'CollisionMap':
            matrix = [[int(i) for i in self.map[j]] for j in range(len(self.map))]
        iLen = len(str(len(matrix)))
        jLen = 0
        for row in matrix:
            maximum = 0
            for i in row:
                x = len(str(i))
                if x > maximum: maximum = x
        if maximum > jLen:
            jLen = maximum
            
        numOfRows = len(matrix[0])//32 + (1 if len(matrix[0])%32!=0 else 0)
        for i, line in enumerate(matrix):
            for j in range(numOfRows):
                row = [f"{k:{jLen}}" for k in line[32*j:32*(j+1)]]
                if j==0:
                    string += f"\n{i:{iLen}}: {' '.join(row)}"
                else:
                    string += f"\n {' '*iLen} {' '.join(row)}"
            
        return f"{self.__class__.__name__}({string}\n)"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.map})"