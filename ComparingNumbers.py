#Assignment
#COMPARING NUMBERS
#Write a program that asks the user for two integers.

#Then, write three separate if/else statements as follows:

#If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

#If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

#If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

#prompt the user 
FirstNumber = int (input("Please input the first number: "))
SecondNumber = int (input("Please input the second number: "))

#Comparing numbers
if FirstNumber>SecondNumber:
    print ("The first number is greater")
else:
    print ("The first number is not greater")
if FirstNumber==SecondNumber:
    print ("The numbers are equal")
else:
    print ("The numbers are not equal")
if SecondNumber>FirstNumber:
    print ("The second number is greater")
else:
    print ("The second number is not greater")    

UserFavoriteAnimal = input ("What is your favorite animal? ") 
MyFavoriteAnimal="Dolphin"

if UserFavoriteAnimal.capitalize()==MyFavoriteAnimal.capitalize():
    print ("That's my favorite animal too!")
else:
    print ("That one is not my favorite.")