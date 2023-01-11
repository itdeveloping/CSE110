
print ("Enter the names and balances of bank accounts (type: quit when done)")
Highest=0
Account=""
AccountList=[]
BalanceList=[]
while Account.lower()!="quit":
    Account=input("What is the name of this account? ")
    if Account.lower()!="quit":
        Balance=float(input("What is the balance? "))
        AccountList.append(Account)
        BalanceList.append(Balance)
        if (Balance>Highest):
            Highest=Balance

Total=0
print ("\nAccount Information:")
for Index, Account in  enumerate(AccountList):
    print (f"{Index}. {Account} - $ {BalanceList[Index]}")
    Total+=BalanceList[Index]

Average=Total/len(AccountList)
print (f"\nTotal: $ {Total:.2f}")
print (f"Average: $ {Average:.2f}")
print (f"Highest Balance: $ {Highest:.2f}")

Update=""
while Update.lower()!="no":
    Update=input("\nDo you want to update an account? ")
    if Update.lower()=="yes":
        Index=int(input("What account index do you want to update? "))
        HighestIndex=len(AccountList)-1
        if Index>=0 or Index<=HighestIndex:
            Balance=float(input("What is the new amount? "))
            BalanceList[Index]=Balance
            Total=0
            print ("\nAccount Information:")
            for Index, Account in  enumerate(AccountList):
                print (f"{Index}. {Account} - $ {BalanceList[Index]}")
                Total+=BalanceList[Index]
        else:
            print("Index out of list! ")

 
Total=0
print ("\nAccount Information:")
for Index, Account in  enumerate(AccountList):
    print (f"{Index}. {Account} - $ {BalanceList[Index]}")
    Total+=BalanceList[Index]


