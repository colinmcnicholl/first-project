# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:36:38 2017

@author: Colin
"""

class Point:
    """Represents a point in 2-D space."""
    
point = Point()


class Rectangle:
    """Represents a rectangle.
    
    Attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rect, dx, dy):
    """The function takes a Rectangle and two numbers, named dx and dy.  It
    changes the location of the rectangle by adding dx to the x co-ordinate of
    corner and dy to the y co-ordinate of corner."""
    box.corner.x += dx
    box.corner.y += dy
    
move_rectangle(box, 20, 50)

"""
Test effect.
"""
print(box.corner.x)
print(box.corner.y)