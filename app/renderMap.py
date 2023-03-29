import pygame

from data import data, GUI
from model.entity import Entity
from .UIComponents.section import Section


def renderMap():
    map=[x for x in Section.all if x.name=='map'][0].surface
    sprites=[]

    for entity in Entity.all:
        sprites.append((
            GUI["textures"][f"{entity.__class__.__name__.lower()}"],
            (entity.x * GUI["texturesSize"], entity.y * GUI["texturesSize"]),
        ))

    map.blits(sprites)


        # # TODO add solution for Body
        # if entity.__class__.__name__ == "Body":
        #     continue

        # GUI["sprites"].append(
        #     (
        #         GUI["textures"][f"{entity.__class__.__name__.lower()}"],
        #         (entity.x * GUI["texturesSize"], entity.y * GUI["texturesSize"]),
        #     )
        # )
        
