
"""
File: Temperature.py
Author: Oscar Rodriguez

Purpose: Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

"""

#begin code

#Ask user for Fahrenheit
Fahrenheit = float( input("What is the temperature in Fahrenheit? ") )

#Calculate Celcius
#To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.
Celsius = (Fahrenheit - 32) * 5 / 9

#Output the result
print(f"The temperature in Celsius is {Celsius:.2f} degrees.")

#end code




