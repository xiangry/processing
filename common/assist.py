
global startX
start = 30
global startY
startY = 30


def transformMathPos( x, y, width, height):
    return x, height - y


def transformMathPosY( y, height):
    return height - y

def show( _text, x, y):
    textSize(10)
    text( _text, x, y)
    
    
def drawPoint(x, y):
    color(100)
    strokeWeight(20)
    point( x * 20, y * 20 )
    strokeWeight(1)
    # rect( x * 20, y* 20 , 20, 20) 
    

def showGrid( width, height ):
    for x in range(30, width, 20):
        line( x, 0, x, height - 30)
        show( str(x / 20 - 1), x - 5, height - 15 )
        
    for y in range(30, height, 20):
        y = transformMathPosY( y, height ) 
        line( 30, y, width, y)
        show( str( (height - y) / 20 - 1), 15 , y  )