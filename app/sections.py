from data import data, GUI

def exitButtonAction(): data['exit']=True
def startSimAction(): data['isSimRunning']=True
def stopSimAction(): data['isSimRunning']=False

def sections():
    w=GUI['windowWidth']
    h=GUI['windowHeight']
    mw=data['simWidth']
    mh=data['simHeight']

    ts=GUI['texturesSize']

    return[
        {
            'name': 'topMenu', 'parent': None,
            'size': (w, 32), 'position':(0, 0),
            'bgc': (40, 40, 40), 'update': False,
        },{
            'name': 'leftMenu', 'parent': None,
            'size': (250, h-30), 'position':(0, 32),
            'bgc': (220, 220, 220), 'update': False,
        },{
            'name': 'simArea', 'parent': None, 
            'size': (w-500, h-30), 'position':(250, 32), 
            'bgc': (50, 50, 50), 'update': False,
        },{
            'name': 'rightMenu', 'parent': None,
            'size': (250, h-30), 'position':(w-250, 32),
            'bgc': (220, 220, 220), 'update': False,
        },{
            'name': 'map', 'parent': 'simArea',     
            'size': (mw*ts, mh*ts), 'position':((w-500-mw*ts)/2, (h-32-mh*ts)/2),
            'bgc': (200, 200, 200), 'update': True,
        },{
            'name': 'exitButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(w-48-4, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Quit', 'action': exitButtonAction,
        },{
            'name': 'startSimButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(0, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Start', 'action': startSimAction,
        },{
            'name': 'stopSimButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(48+1, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Stop', 'action': stopSimAction,
        },
    ]