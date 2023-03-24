from model.entity import Entity
from model.cell import Cell

print(Entity.all)
print(Cell.all)
Cell.all[0].energy = -20
print(Entity.all)
