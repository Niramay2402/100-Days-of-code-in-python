# Leap year or not
year = int(input("Which year do you want to check? "))

leapYear = year%4

if(leapYear == 0):
    print("Leap year.")
else:
    print("Not leap year.")