class forwards():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self, distance):
        self.turtle.forward(distance)
        
class backwards():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self, distance):
        self.turtle.back(distance)

class rightTurn():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self, angle):
        self.turtle.rt(angle)

class leftTurn():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self, angle):
        self.turtle.lt(angle)
        
class penUp():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self):
        self.turtle.pu()

class penDown():
    def __init__(self, turtle):
        self.turtle = turtle
        
    def __call__(self):
        self.turtle.pd()
