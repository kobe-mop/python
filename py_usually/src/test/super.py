class Foo():
    def __init__(self):
        self.frobnicate = "a"
        self.frotz = "b"

class Bar(Foo):
    def __init__(self):
        super().__init__()
        self.frazzle = 34
        
new = Bar() 
print (new.frobnicate) 
print (new.frotz)
print (new.frazzle)  