from turtle import *
shape('turtle')

def circleOfSquares(length=150):
    for squares in range(60):
        for i in range(4):
            forward(length)
            right(90)
        right(5)

