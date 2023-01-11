
"""
File: MealPriceCalculator.py
Author: Oscar Rodriguez

Purpose: Write a program to calculate the price of a meal.
"""
#begin code
print("Hi ! Welcome to our Meal Price Calculator.")

#prompt food princes
print("\nType the following prices:")
ChildMeal = float(input ("What is the price of a child's meal? "))
AdultMeal = float(input ("What is the price of an adult's meal? "))
DrinkPrice = float(input ("What is the price of a drink? "))
AppetizerPrice = float(input("What is the prince of an appetizer? "))

#consumed quantity
print("\nType the following information: ")
NumberOfChildren = int (input ("How many children are there? "))
NumberOfAdults=int(input("How many adults are there? "))
Drinks = int (input ("How many drinks were served? "))
Appetizers = int (input ("How many appetizers were served? "))

#Tax rate and tip percentage
TaxRate = float (input("\nWhat is the sales tax rate? ")) 
TipPercentage= float(input("What is the tip percentage? "))

#operations
ChildsSubtotal=ChildMeal*NumberOfChildren
AdultsSubtotal=AdultMeal*NumberOfAdults
DrinksSubtotal=DrinkPrice*Drinks
AppetizerSubtotal=AppetizerPrice*Appetizers
Subtotal = ChildsSubtotal+AdultsSubtotal+DrinksSubtotal+AppetizerSubtotal
SalesTax= Subtotal*TaxRate/100
Total = Subtotal+SalesTax
Tip=Total*TipPercentage/100
GrandTotal=Total+Tip

#display results
print("-----------------")
print (f"Subtotal: ${Subtotal:.2f}")
print (f"Sales Tax: ${SalesTax:.2f}")
print (f"Tip: ${Tip:.2f}")
print (f"Total: ${GrandTotal:.2f}")
print("")

#prompt payment and display change
Payment= float(input("What is the payment amount? "))
Change= Payment-GrandTotal
print (f"\nChange: ${Change:.2f}")

#output order details
print("-----------------")
print("\nOrder details:")
print(f"{'Description':15} {'Price':>7} {'Qty':>6} ")
print(f"{'Child meal':15} {ChildMeal:>7.2f} {' x':2} {NumberOfChildren:3}  {ChildsSubtotal:>8.2f}")
print(f"{'Adult meal':15} {AdultMeal:>7.2f} {' x':2} {NumberOfAdults:3}  {AdultsSubtotal:>8.2f}")
print(f"{'Drink':15} {DrinkPrice:>7.2f} {' x':2} {Drinks:3}  {DrinksSubtotal:>8.2f}")
print(f"{'Appetizer':15} {AppetizerPrice:>7.2f} {' x':2} {Appetizers:3}  {AppetizerSubtotal:>8.2f}")
print ("________________________________________")
print (f"{'Subtotal:':30} ${Subtotal:>8.2f}")
print (f"{'Sales Tax':30} ${SalesTax:>8.2f}")
print (f"{'Tip:':30} ${Tip:>8.2f}")
print (f"{'Total:':30} ${GrandTotal:>8.2f}")
print (f"{'Payment:':30} ${Payment:>8.2f}")
print (f"{'Change:':30} ${Change:>8.2f}")

#final salutation
print("\nThank you for using our information systems. See you soon!")

#end of code

#Comments:
#I added a couple of products like drinks and appetizer in the program menu
#I displayed the order details like a Supermarket receipt witi final salutation