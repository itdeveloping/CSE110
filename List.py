

Item=""
ItemList=[]
while Item.lower()!="quit":
    Item=input("Please enter the items of the shopping list (type: quit to finish):")
    if Item.lower()!="quit":
        ItemList.append(Item)

print ("The shopping list is:")
for i in ItemList:
    print (f"{i}")

print ("The shopping list with indexes is:")
for index, item in enumerate(ItemList):
    print (f"{index}. {item}")

"""
Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is:
0. Milk
1. Bread
2. Apples
3. Carrots
"""
