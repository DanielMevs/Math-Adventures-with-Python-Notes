from turtle import *
shape('turtle')

def starSpiral(length=60):
    for i in range(60):
        for j in range(5):
            forward(length)
            right(180 - 36)
        length += 6
        left(5)

