t = 0
def setup():
    size(600,600)
    rectMode(CENTER)

def draw():
    #translate(200,200);
    #rotate(radians(20));
    #rect(50,100,100,60)
    
    #for circle non-animated
    '''for i in range(12):
        ellipse(200,0,50,50)
        rotate(radians(360/12))'''
    
    global t
    #set background white
    background(255)
    translate(width/2, height/2)
    rotate(radians(5*t))
    for i in range(12):
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(5*t))
        rect(0,0,50,50)
        popMatrix() #return to the saved orientation
        rotate(radians(360/12))
    t+=.01
    

        
