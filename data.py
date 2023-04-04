# class Tmp:
#     def __init__(self):
#         self.map = [[]]
    
data={
    'exit':False,
    'isSimRunning': False,

    'simHeight': 64,
    'simWidth': 128,

    'frameRate': 30,
    'debugShowDelay': 1000,
    'modelIterationDelay': 50,

    'id': 0,
    'tick': 1,
    
    'initialCellNumber': 4,
    'initialFoodNumber': 200,
    # 'initialCellNumber':100,
    # 'initialFoodNumber': 30,
    
    # 'OrganicMatter': Tmp()
}

environment={}

GUI={
    'windowWidth': 1920,
    'windowHeight': 1080-64,

    'windowTitle': "Simulation",
    'sprites':[],
    'texturesSize': 8,
    'textures':{},
    'topBarButtons':[]
}
 