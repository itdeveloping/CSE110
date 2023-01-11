bank=[]
balance=[]

account=""

while account!="quit":
    account=input("What's the name of this account? ")    
    if account!="quit":
        balance_amount=float(input("What is the balance? "))
        bank.append(account)
        balance.append(balance_amount)

print("Account information: ")
total=0
high_balance=0
for i in range(len(bank)):
    account_bank=bank[i]
    amount=balance[i]
    if amount>high_balance:
        high_balance=amount
        index_balance=i

    total=total+amount    
    print(f"{account_bank} - ${amount} ")
average=total/len(bank)
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
print(f"Highest balance: {bank[index_balance]} - ${high_balance:.2f}")


answer=input("Do you want to update an account? yes/no ")

while answer=="yes":

    index_update=int(input("What account index do you want to update? "))
    new_amount=input("What is the new amount? ")  
 
    balance[index_update]=new_amount    
    answer=input("Do you want to update an account? yes/no ")

print("Account information: ")

for i in range(len(bank)):
    account_bank=bank[i]
    amount=balance[i]
    print(f"{account_bank} - ${amount} ")


print(f"{'033[1;31m'} The total price of the items in the shopping cart is: {amount:.2f} ")