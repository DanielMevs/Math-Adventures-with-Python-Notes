#a function that takes an integer as an argument
#and makes the turtle draw a polygon with that
#integer's number of sides.

from turtle import *
shape('turtle')

def polygon(length=150):
    sides = int(input("Enter the number of sides for this polygon: "))
    for x in range(sides):
        forward(length)
        right(360/sides)