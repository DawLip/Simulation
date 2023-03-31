# import pygame

# from model.entities.importEntities import Entity

class Test:
    all=[]
    def __init__(self, foo: int = 'XD'):
        self.__foo = foo
        self.child = []
        
        Test.all.append(self)
        
    @property
    def foo(self):
        return self.__foo
    
    def fun(self):
        print('s')
        self.child.append(Test(2))
    # @foo.setter
    # def foo(self, newFoo):
    #     assert isinstance(newFoo, int), "foo must be an int"
    #     print('setter')
    #     self.__foo = newFoo
        
    def __repr__(self) -> str:
        return f"Test({self.foo}, {self.child})"

Test(1)
print(Test.all[0])
Test.all[0].fun()
print(Test.all[0])
