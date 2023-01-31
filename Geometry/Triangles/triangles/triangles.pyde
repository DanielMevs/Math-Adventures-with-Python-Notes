def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
    
t = 0

def draw():
    global t
    background(255)
    translate(width/2,height/2)
    #rainbowObj = rainbow()
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+2*i*360/90))
        #tri(100, rainbowObj)
        tri(100, i)
        popMatrix()
    
    # rotate(radians(t))
    # #triangle(0,0,100,100,200,-200)
    # tri(200) #draw the equilateral triangle
    t += 0.5
    
    
"""def tri(length, rainbowObj):
    '''Draws an equilateral triangle
    around center of triangle'''
    noFill()
    r, g, b = next(rainbowObj)
    stroke(r, g ,b)
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)"""
    
def tri(length, i):
    '''Draws an equilateral triangle
    around center of triangle'''
    noFill()
    stroke(i*3.14, 255, 255)
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
'''
90/6 =15
256/15 = 17
'''
'''def rainbow():
    r, g, b = 255, 0, 0
    for g in range(0, 256, 17):
        yield r, g, b
    for r in range(255, -1, -17):
        yield r, g, b
    for b in range(0, 256, 17):
        yield r, g, b
    for g in range(255, -1, -17):
        yield r, g, b
    for r in range(0, 256, 17):
        yield r, g, b
    for b in range(255, -1, -17):
        yield r, g, b'''
