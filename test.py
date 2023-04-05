from model.environment.CollisionMap import CollisionMap

obj = CollisionMap()
foo = obj.map
foo[-1][-1]=1
obj.map = foo
print(obj)
