import assist

def setup():
    size(640, 480)
    background(155, 155, 155)
    
def draw():
    assist.showGrid( width, height)
    assist.drawPoint( 5, 5 )     
    
def mousePressed():
    saveFrame("/Users/gxs/Desktop/output.png")