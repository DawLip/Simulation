class A:
    def __init__(self):
        self.x=3
        
a=A()
print(props([i for i in a.__dict__.keys() if i[:1] != '_']))
