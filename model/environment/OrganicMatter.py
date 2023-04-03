# from data import data
 
data={
    'exit':False,
    'isSimRunning': False,

    'simHeight': 64,
    'simWidth': 128,}

class OrganicMatter:
    def __init__(self, map=[[_ for _ in range(data['simWidth'])] for _ in range(data['simHeight'])]):
        assert isinstance(map, list) and len(map)==data['simHeight'] and len(map[0])==data['simWidth'], "map must be a list and height == data['simHeight'] and width==data['simWidth']"
        self.map = map
        
    def __str__(self):
        string = ''
        iLen = len(str(data['simHeight']))
        jLen = len(str(self.map[0][-1]))
        numOfRows = len(self.map[0])//32 + (1 if len(self.map[0])%32!=0 else 0)
        for i, line in enumerate(self.map):
            for j in range(numOfRows):
                row = [f"{k:{jLen}}" for k in line[32*j:32*(j+1)]]
                if j==0:
                    string += f"\n{i:{iLen}}: {' '.join(row)}"
                else:
                    string += f"\n {' '*iLen} {' '.join(row)}"
            
        return f"OrganicMatter({string}\n)"
    
    def __repr__(self):
        string = ''
        for i, line in enumerate(self.map):
            string += f'\n{i}: {line}'
        return f"{string}"
