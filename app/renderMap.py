import pygame

from data import data, GUI
# from model.food import Food
# from model.cell import Cell
from model.entity import Entity

def renderMap():
    for entity in Entity.all:
        GUI['sprites'].append((
            GUI['textures'][f'{entity.__class__.__name__.lower()}'],
            (entity.x*GUI['texturesSize'], entity.y*GUI['texturesSize'])
        ))
        
    # for cell in Cell.all:
    #     GUI['sprites'].append((
    #         GUI['textures']['cell'],
    #         (cell.x*GUI['texturesSize'], cell.y*GUI['texturesSize'])
    #     ))

    # for food in Food.all:
    #     GUI['sprites'].append((
    #         GUI['textures']['food'],
    #         (food.x*GUI['texturesSize'], food.y*GUI['texturesSize'])
    #     ))