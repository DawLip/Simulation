# import pygame

# from model.entities.importEntities import Entity

class Test:
    all=[]
    def __init__(self, foo: int):
        self.foo = foo
        
    def fun(self):
        self.foo=self.foo+1
        
    @property
    def foo(self):
        return self.__foo
    @foo.setter
    def foo(self,newValue):
        print('auu')
        self.__foo = newValue
        
    def __repr__(self) -> str:
        return f"Test({self.foo})"

obj = Test(1)
print(obj)
obj.fun()
print(obj)
