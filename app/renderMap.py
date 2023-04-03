from model.entities.importEntities import Entity
from .UIComponents.UIComponents import Section

from data import GUI, data

def renderMap():
    map=[x for x in Section.all if x.name=='map'][0]
    sprites=[]
    # sprites2=[]

    # for i, line in enumerate(data['OrganicMatter'].map):
    #     for j, px in enumerate(line):
    #         sprites2.append((
    #         GUI["textures"]["OrganicMatter"],
    #         (
    #             map.x + j * GUI["texturesSize"], 
    #             map.y + i * GUI["texturesSize"]
    #         ),
    #     ))
    
    for entity in Entity.all:
        sprites.append((
            GUI["textures"][f"{entity.__class__.__name__.lower()}"],
            (
                map.x + entity.x * GUI["texturesSize"], 
                map.y + entity.y * GUI["texturesSize"]
            ),
        ))

    # GUI['window'].blits(sprites2)
    GUI['window'].blits(sprites)
        
