""""
File: ShoppingCart.py
Author: Oscar Rodriguez

Purpose: create a program that stores a list of products in a shopping cart along with their prices.
"""
# Begin of code

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[0m'

#Declare Lists
ItemNames=[]
ItemPrices=[]

#Welcome message
print (f"{bcolors.WARNING}-------------------------------------------")
print (f"{bcolors.OKCYAN}Welcome to the Shopping Cart Program v1.0! {bcolors.OKBLUE}by Oscar Rodriguez SoftDev")
#Ask the user for an option
print (f"\n{bcolors.OKGREEN}Select one of the following: ")
print ("1. Add item")
print ("2. View cart")
print ("3. Remove item")
print ("4. Compute total")
print ("5. Quit")

Option=int(input("Please enter an action: "))

#Start checking the action
while Option!=5:
    if Option==1: #Add item
        ItemName=input(F"\n{bcolors.WHITE}What item would you like to add? ")
        ItemPrice=float(input(f"What is the price of '{ItemName}'? "))
        ItemNames.append(ItemName)
        ItemPrices.append(ItemPrice)
        print (f"\n{bcolors.WARNING}-----------------> '{ItemName}' has been added to the cart <-----------------")

    elif Option==2: #View cart
        print(f"\n{bcolors.OKCYAN}--------------------------------------")
        if len(ItemNames)!=0: #Check if there is items in the shopping cart
            print (f"{bcolors.OKCYAN}The contents of the shopping cart are:")
            Tab=len(max(ItemNames, key=len))+2
            for Index, Item in enumerate(ItemNames):
                print (f"{Index+1}. {Item:<{Tab}} - $ {ItemPrices[Index]:>2.2f}")
        else:
            print(f"{bcolors.OKCYAN}Your cart is empty!")
        print("--------------------------------------")

    elif Option==3: #Remove item
        if len(ItemNames)!=0: #Check if there is items in the shopping cart
            Index=int(input(f"\n{bcolors.WARNING}Which item would you like to remove? "))
            Index-=1
            HighestIndex=len(ItemNames)-1
            if Index>=0 and Index<=HighestIndex: #Check if the item to remove is in the list
                Item=ItemNames[Index]
                ItemNames.pop(Index)
                ItemPrices.pop(Index)
                print(f"-----------------> '{Item}' has been removed! <-----------------")
            else:
                print(f"\n########## Sorry {Index+1} is out of list! ##########")

        else:            
            print(f"{bcolors.WARNING}--------------------------------------")
            print(f"{bcolors.WARNING}Your cart is empty! ")
            print(f"{bcolors.WARNING}--------------------------------------")
   
    elif Option==4: #compute total
        print(f"\n{bcolors.OKCYAN}--------------------------------------")
        if len(ItemNames)!=0: #Check if there is items in the shopping cart
            Total=0
            for Price in ItemPrices:
                Total+=Price
            print (f"{bcolors.OKCYAN}The total price of the {len(ItemNames)} item(s) in your shopping cart is $ {Total:.2f}")
        else:
            print(f"{bcolors.OKCYAN}Your cart is empty! ")
        print(f"{bcolors.OKCYAN}--------------------------------------")

    elif Option<1 or Option>5: #if user types not a valid option
        print (f"\n{bcolors.WARNING}<<<<<<< Not a valid option! >>>>>>>>")
    print (f"\n{bcolors.OKGREEN}Select one of the following: ")
    print ("1. Add item")
    print ("2. View cart")
    print ("3. Remove item")
    print ("4. Compute total")
    print ("5. Quit")
    Option=int(input("\nPlease enter an action: "))

#Display a final message
print (f"\n{bcolors.WHITE}Thank you for using our system. Goodbye!")
print ("-----------------------------------------")
#end of code