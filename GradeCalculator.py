"""
File: MealPriceCalculator.py
Author: Oscar Rodriguez

Purpose: Write a program that determines the letter grade.

Overview
Write a program that determines the letter grade for a course according to the following scale:
A >= 90

B >= 80

C >= 70

D >= 60

F < 60
"""
#begin code
GradePercent = int (input("Please type your grade percentage: "))
print ("")
#if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.
if GradePercent>=90:
    Letter="A"
elif GradePercent>=80:
    Letter="B"
elif GradePercent>=70:
    Letter="C"
elif GradePercent>=60:
    Letter="D"
else:
    Letter="F"

Result = GradePercent % 10
if Result>=7:
    Sign="+"
elif Result<=3:
    Sign="-"
else:
    Sign=""

if Letter == "A" and Sign == "+":
    Sign=""
if Letter == "F":
    Sign = ""

print (f"Your letter grade is {Letter}{Sign}")

if GradePercent>=70:
    print ("Congratulations, you passed! Keep it up!")
else:
    print ("Sorry, you failed! Don't get discouraged, keep trying! ")   
