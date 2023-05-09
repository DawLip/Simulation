data = {
    'exit': False,
    'isSimRunning': False,
    'isMakeStep': False,
    'isModelReady': False,
    'isSimRestart': False,

    'simHeight': 64*2,
    'simWidth': 128*2,

    'frameRate': 0,
    'GUIframeRate': 30,
    'debugShowDelay': 1000,
    'modelIterationDelay': 50,

    'id': 0,
    'tick': 1,
    'seed': '7628712',

    'initialCellNumber': 10,
    'initialFoodNumber': 300,
    # 'initialCellNumber':100,
    # 'initialFoodNumber': 30,

    # 'OrganicMatter': Tmp()
    'CollisionMap': object(),

    'IsKeyPressedEvent': False,
    'keyPressed': None,
    
    'selectedEntity': None
}

environment = {}

GUI = {
    'windowWidth': 1920,
    'windowHeight': 1080-64,

    'windowTitle': "Simulation",
    'windows': [],
    'sprites': [],
    'texturesSize': 8,
    'textures':{},
    'topBarButtons':[],
    
    'colors':{
        '0 color': '#1E1E26',
        '1 color': '#282834',
        '2 color': '#313140',
        '3 color': '#3B3B4D',
        
        '0 borderColor': '#14141A',
        '1 borderColor': '#1D1D26',
        '2 borderColor': '#272733',
        '3 borderColor': '#454559',
        
        'Font White': '#E4E4E7',
    }
}

debug = {
    'tickCounter': 0,
    'timerResult': 0
}

