data={
    'exit':False,
    'isSimRunning': True,

    'simHeight': 64*2,
    'simWidth': 128*2,

    'frameRate': 20,
    'GUIframeRate': 10,
    'debugShowDelay': 1000,
    'modelIterationDelay': 50,

    'id': 0,
    'tick': 1,
    
    'initialCellNumber': 4,
    'initialFoodNumber': 200,
    # 'initialCellNumber':100,
    # 'initialFoodNumber': 30,
    
    # 'OrganicMatter': Tmp()
    'CollisionMap': object(),

    'IsKeyPressedEvent': False,
    'keyPressed':None
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
 
debug={
    't1': 0
}