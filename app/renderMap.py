from model.entities.importEntities import Entity
from .UIComponents.UIComponents import Section

from data import GUI

def renderMap():
    map=[x for x in Section.all if x.name=='map'][0]
    sprites=[]

    for entity in Entity.all:
        sprites.append((
            GUI["textures"][f"{entity.__class__.__name__.lower()}"],
            (
                map.x + entity.x * GUI["texturesSize"], 
                map.y + entity.y * GUI["texturesSize"]
            ),
        ))

    GUI['window'].blits(sprites)
        
