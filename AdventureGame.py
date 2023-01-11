
"""
File: Calculations.py
Author: Oscar Rodriguez

Purpose: Practice using if statements.
"""

#begin code
#output a welcome message 
print ("Hi! Welcome to the Adventure Game v1.0. Please answer each question according to the words in CAPS. Enjoy it!\n")

#I am going to use three variables to control the user types one of two answers on each question
FlagOne=0
while FlagOne==0:
    ChoiceOne = input ("After working hard all this year, your are on vacations, where do you want to head to, NORTH or SOUTH? ").upper()
    if ChoiceOne=="NORTH":
        FlagOne=1
        FlagTwo=0
        while FlagTwo==0:
            ChoiceTwo = input ("Now that you chose going to north, what would you like to do, SHOPPING or VISITING friends/relatives? ").upper()
            if ChoiceTwo=="SHOPPING":
                FlagTwo=1
                FlagThree=0
                while FlagThree==0:
                    ChoiceThree = input ("Great! Shopping is a good choice. Where do you want to go and spend some money, DILLARD'S or MACY'S? ").upper()
                    if ChoiceThree=="DILLARD'S":
                        print ("\nHave a great day at Dillard's store.")
                        FlagThree=1
                    elif ChoiceThree=="MACY'S":
                        print ("\nHave a nice day at Macy's store.")
                        FlagThree=1
            elif ChoiceTwo=="VISITING":
                FlagTwo=1        
                FlagThree=0
                while FlagThree==0:
                    ChoiceThree = input ("Wonderful! Long time you haven't seen some loved people. Who do you want to visit, RELATIVES or FRIENDS? ").upper()
                    if ChoiceThree=="RELATIVES":
                        print ("\nEnjoy your time with your relatives!")
                        FlagThree=1
                    elif ChoiceThree=="FRIENDS":
                        print ("\nYour friend will be happy to see you again!")
                        FlagThree=1
    elif ChoiceOne=="SOUTH":
        FlagOne=1
        FlagTwo=0
        while FlagTwo==0:
            ChoiceTwo = input ("Now that you chose going to south, where do you want to spend time with your family, BEACH or DOWNTOWN? ").upper()
            if ChoiceTwo=="BEACH":
                FlagTwo=1
                FlagThree=0
                while FlagThree==0:
                    ChoiceThree = input ("Awesome! This place's beach is amazing. What would you prefer, SWIM or WALK? ").upper()
                    if ChoiceThree=="SWIM":
                        print ("\nHave a great day swimming at the beach!")
                        FlagThree=1
                    elif ChoiceThree=="WALK":
                        print ("\nEnjoy taking a walk over the beach's sand!")
                        FlagThree=1
            elif ChoiceTwo=="DOWNTOWN":
                FlagTwo=1
                FlagThree=0
                while FlagThree==0:
                    ChoiceThree = input ("Very good! Downtown have several places to visit. Where do you want to have some fun with your family, the MOVIE TEATHER or the MOVIE TEATHER? ").upper()
                    if ChoiceThree=="MOVIE TEATHER":
                        print ("\nHave a great time watching the premiere!")
                        FlagThree=1
                    elif ChoiceThree=="MOVIE TEATHER":
                        print ("\nEnjoy this family time at the museum!")
                        FlagThree=1

#output a resume of the user's choices
print (f"Your choices: {ChoiceOne} -> {ChoiceTwo} -> {ChoiceThree}")                

#end of code

