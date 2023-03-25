import pygame

from data import data, GUI
from model.entity import Entity


def renderMap():
    for entity in Entity.all:
        # TODO add solution for Body
        if entity.__class__.__name__ == "Body":
            continue
        GUI["sprites"].append(
            (
                GUI["textures"][f"{entity.__class__.__name__.lower()}"],
                (entity.x * GUI["texturesSize"], entity.y * GUI["texturesSize"]),
            )
        )
