# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:19:13 2017

@author: Colin
"""

"""
Exercise section 15.6 think python.
write a version of move_rectangle that creates and returns a new Rectangle
instead of modifying the old one.
"""

"""
create a type called Point that represents
a point in two-dimensional space.
"""

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """Represents a rectangle.
    
    Attributes: width, height, corner.
    """

def move_rectangle(rect, dx, dy):
    """The function takes a Rectangle and two numbers, named dx and dy.  It
    changes the location of the rectangle by adding dx to the x co-ordinate of
    corner and dy to the y co-ordinate of corner."""
    box.corner.x += dx
    box.corner.y += dy

"""
To represent a rectangle, you have to instantiate a Rectangle object and
assign values to the attributes:
"""

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

import copy

def move_rectangle4(rect, dx, dy):
    """The function takes a Rectangle and two numbers, named dx and dy.
    Creates and returns a new rectangle, in a new location.  The new location
    is created by adding dx to the x co-ordinate of
    corner and dy to the y co-ordinate of corner."""
    box4 = copy.deepcopy(box)
    print(box4 != box)  # check have created a deep copy
    print(box4.corner is box.corner)  # double check have created a deep copy
    move_rectangle(box4, dx, dy)
    
"""Test result"""
move_rectangle4(box, 20, 20)
print(box.corner.x)
print(box.corner.y)