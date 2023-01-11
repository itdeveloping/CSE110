
"""
File: Calculations.py
Author: Oscar Rodriguez

Purpose: Practice using mathematical expressions.
"""

#Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:
#Make sure that your program can appropriately handle decimal values as well as whole numbers.
#Square—The area is the length of a side squared.
#Rectangle—The area is the length multiplied by the width.
#Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.


# Import math Library
import math

Length=float(input ("What is the length of a side of the square (cm)? "))
SquareArea=Length*Length
print (f"The area of the square is: {SquareArea} square centimeters" )
print()

Length=float(input ("What is the length of rectangle (cm)? "))
Width=float(input ("WWhat is the width of the rectangle (cm)? "))
RectangleArea=Length*Width
print (f"The area of the rectangle is: {RectangleArea} square centimeters")
print()

Radius=float(input ("What is the radius of the circle (cm)? "))
AreaCircle=math.pi*Radius**2
print(f"The area of a circle is: {AreaCircle} square centimeters")

SquareArea=SquareArea/100
RectangleArea=RectangleArea/100
AreaCircle=AreaCircle/100
print()
print (f"The area of the square in square meters is : {SquareArea}" )
print (f"The area of the rectangle in square meters is : {RectangleArea}")
print(f"The area of a circle in square meters is : {AreaCircle}")
