
"""
File: Age.py
Author: Oscar Rodriguez

Purpose: Practice using mathematical expressions.
"""

#Write a program that does the following:

#Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

#Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

#Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.



Age=int(input ("How old are you? "))
print (f"On your next birthday, you will be {Age+1}.")

print("")
Cartons= int(input("How many egg cartons do you have? "))
TotalEggs=Cartons*12
print(f"You have {TotalEggs} eggs")

print("")
Cookies=int(input("How many cookies do you have? "))
People=int(input("How many people are there? "))
print (f"Each person may have {Cookies/People} cookies")
# Import math Library
import math
Circle=math.pi()*2
print(f"The area of a circle is: {Circle}")