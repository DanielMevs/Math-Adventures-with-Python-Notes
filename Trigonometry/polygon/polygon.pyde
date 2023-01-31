def setup():
    size(600, 600)

def draw():
    # beginShape()
    # vertex(100, 100)
    # vertex(100, 200)
    # vertex(200, 200)
    # vertex(200, 100)
    # vertex(150, 50)
    # endShape(CLOSE)
    translate(width/2, height/2)
    polygon(3, 100)
    # beginShape()
    # for i in range(8):
    #     #replace abv w/ range(6): hexagon
    #     # vertex(100*cos(radians(60*i)),
    #     #        100*sin(radians(60*i)))
    #     vertex(100*cos(radians(45*i)),
    #            100*sin(radians(45*i)))
    # endShape(CLOSE)
def polygon(sides, sz):
    '''draws a polygon given the number
    of sides and length from the center'''
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i*step),
               sz*sin(i*step))
    endShape(CLOSE)
    
