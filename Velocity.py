
"""
File: Speed.py
Author: Oscar Rodriguez

Purpose: Determine how fast an object will fall.
"""


#Begin code
#import Math Library
import math

#Welcome message
print ("Welcome to the velocity calculator. Please enter the following: ")

#Prompts user
m = float ( input("Mass (in kg): "))
g = float ( input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter: "))
t = int ( input("Time (in seconds): "))
p = float ( input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float (input ("Cross sectional area (in m^2): "))
C = float ( input ("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Calculate Inner Value and Velocity
"""""

The function that computes the speed after "t" seconds have elapsed is given by:

v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

Where:

m = mass (in kg)
g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
t = time (in seconds)
c = 1/2 p A C
p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
A = cross sectional area of projectile (in square meters)
C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)
exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

"""""
c = (1 / 2) * p * A * C
VelocityAtTime = math.sqrt(m*g/c) * (1 - math.exp ((-math.sqrt(m*g*c)/m*t )))

#Output the results
print (f"\nThe inner value of c is: {c:.3f}")
print (f"The velocity after {t} seconds is: {VelocityAtTime:.3f} m/s")

#End code
