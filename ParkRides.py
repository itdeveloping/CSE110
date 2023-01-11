
"""
File: ParkRides.py
Author: Oscar Rodriguez

Purpose: For this assignment, you'll work as a team to write a program for a fictitious amusement park ride.
"""

"""
THE SCENARIO: RIDER REQUIREMENTS
The local amusement park has just installed a new ride. Because of its speed and extreme twists and turns, it has very strict requirements for the riders, especially as it pertains to children or other shorter riders.

To help the ride attendants follow the rules, you've been asked to write an app to help them know if the riders are acceptable for the car.

The basic rules are as follows:

#1 No one under 36 inches may ever ride, either by themselves or with another rider.
#2 Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
#3 If there are two riders and one of them is at least 18 years old, they may ride together.

Stretch rules:
#1 If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
#2 If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
#3 If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)
"""
from ast import While

#begin code

#prompts for first rider
Age1=int(input("What is the age of the first rider? " ))
Height1=int(input("What is the height of the first rider? "))
FlagTwo=False
if Age1>=12 and Age1<=17:
    while FlagTwo==False:
        FirstRiderGP=input("Does the first rider have a golden passport (yes/no)? ") #Stretch rule no. 2
        if FirstRiderGP.lower()=="yes":
            FlagTwo=True
        if FirstRiderGP=="no":
            FlagTwo=True

print("")
FlagOne=False
while FlagOne==False:
    AnotherRider=input("Is there a second rider (yes/no)? " )
    if AnotherRider.lower()=="yes":
        Flag=True
        #prompts for second rider
        Age2=int(input("What is the age of the second rider? "))
        Height2=int(input("What is the height of the second rider? " ))
        if Age2>=12 and Age2<=17:
            FlagTwo=False
            while FlagTwo==False:
                SecondRiderGP=input("Does the second rider have a golden passport (yes/no)? ") #Stretch rule no. 2
                if SecondRiderGP.lower()=="yes":
                    FlagTwo=True
                if SecondRiderGP=="no":
                    FlagTwo=True
        FlagOne=True
    elif AnotherRider.lower()=="no":
        FlagOne=True
CanRide=False

#apply rules
if AnotherRider=="no":
    if Age1>=18 and Height1>=62: #Basic Rule no. 2
        CanRide=True
    if Age1>=12 and Age1<=17 and FirstRiderGP=="yes" and Height1>=62: #Stretch rule no. 2
        CanRide=True
    if Height1<36: #Basic Rule no. 1
        CanRide=False
    
else:
    if Age1>=18 or Age2>=18: #Basic Rule no. 3
        CanRide=True
    if Age1>=12 and Age2>=12 and Height1>=52 and Height2>=52: #Stretch  Rule no. 1
        CanRide=True
    if Age1>=12 and Age1<=17 and FirstRiderGP=="yes" and Height1>=62: #Stretch rule no. 2
        CanRide=True
    if Age2>=12 and Age2<=17 and SecondRiderGP=="yes" and Height2>=62: #Stretch rule no. 2
        CanRide=True
    if Height1<36 or Height2<36: #Basic Rule no. 1
        CanRide=False
    if Age1>=16 and Age2>=14 or Age1>=14 and Age2>=16: #Stretch rule no. 3
        CanRide=True

#output results
if CanRide:
    print ("Welcome to the ride. Please be safe and have fun!")
else:
    print ("Sorry, you may not ride.")

#end code