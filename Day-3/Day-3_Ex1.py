# Odd or Even number Check
number = int(input("Which number do you want to check? "))

#number = int(input("Enter the Number:"))

No = number%2

if(No == 1):
    print("This is an odd number.")
else:
    print("This is an even number.")