# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


True_1 =0
True_2 =0
Love_1 = 0
Love_2 = 0

for x in name1:
    if(x == "T" or x == "t" or x == "U" or x == "u" or x == "R" or x == "r" or x == "E" or x == "e"):
        True_1 = True_1 +1
    else:
        p=1


for y in name2:
    if(y == "T" or y == "t" or y == "R" or y == "r" or y == "U" or y == "u" or y == "E" or y == "e"):
        True_2 = True_2 +1
    else:
        p=1

True_Total = True_2 + True_1
print(True_Total)


for a in name1:
    if(a == "L" or a == "l" or a == "O" or a == "o" or a == "V" or a == "v" or a == "E" or a == "e"):
        Love_1 = Love_1 +1
    else:
        p=1


for b in name2:
    if(b == "L" or b == "l" or b == "O" or b == "o" or b == "V" or b == "v" or b == "E" or b == "e"):
        Love_2 = Love_2 +1
    else:
        p=1

Love_Total = Love_2 + Love_1
print(Love_Total)

Love_values = (f"{True_Total}{Love_Total}")
Love_value = int(f"{True_Total}{Love_Total}")

if(Love_value < 10 or Love_value > 90):
    print("Your score is " + Love_values +", you go together like coke and mentos.")
    
elif(Love_value > 40 and Love_value < 50):
    print("Your score is " + Love_values +", you are alright together.")
else:
    print("Your score is " + Love_values +".")