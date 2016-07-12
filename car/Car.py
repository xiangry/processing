class Car:
    c = color(0)
    xpos = 0
    ypos = 0
    xspeed = 1
    
    def __init__(self, c, x, y ):
        self.c = color(c)
        self.xpos = x
        self.ypos = y
        
    def display(self):
        rectMode(CENTER)
        fill(self.c)
        rect(self.xpos, self.ypos, 20, 10)
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed
        if self.xpos > width :
            self.xpos = 0
            
        