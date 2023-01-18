# Pizza Bill Counting with add ons
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

TotalBill = 0
#for the size of pizza
sizeBill = 0
PepBill = 0
CheeseBill = 0

if(size == "S" or size == "s"):
    sizeBill = 15
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        PepBill = 2
    else:
        PepBill = 0

    if(extra_cheese == "Y" or extra_cheese == "y"):
        CheeseBill = 1
    else:
        CheeseBill = 0

elif(size == "M" or size == "m"):
    sizeBill = 20
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        PepBill = 3
    else:
        PepBill = 0

    if(extra_cheese == "Y" or extra_cheese == "y"):
        CheeseBill = 1
    else:
        CheeseBill = 0

elif(size == "L" or size == "l"):
    sizeBill = 25
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        PepBill = 3
    else:
        PepBill = 0

    if(extra_cheese == "Y" or extra_cheese == "y"):
        CheeseBill = 1
    else:
        CheeseBill = 0

TotalBill = sizeBill + PepBill + CheeseBill

print(f"Your final bill is: ${TotalBill}.")


