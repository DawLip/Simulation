import pygame

from data import data, GUI, entities

def renderMap():
    for cell in entities['cells']:
        GUI['sprites'].append((
            GUI['textures']['cell'],
            (cell.x*GUI['texturesSize'], cell.y*GUI['texturesSize'])
        ))

    for food in entities['food']:
        GUI['sprites'].append((
            GUI['textures']['food'],
            (food.x*GUI['texturesSize'], food.y*GUI['texturesSize'])
        ))