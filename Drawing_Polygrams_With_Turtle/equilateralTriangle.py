from turtle import *
shape('turtle')
def triangle(sidlength=200):
    for i in range(20):
        forward(sidlength)
        #subract by 180 to account for internal angle
        right(180-60)
#triangle()