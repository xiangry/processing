from Car import Car

global myCar
    
def setup():
    size(200, 200)
    global myCar
    myCar = Car(200, 0, 100)
    
def draw():
    background(0)
    global myCar
    myCar.display()
    myCar.drive()
    
        