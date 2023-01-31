"""
Program Requirements

- Print Report
- Check resources sufficient?
- Process Coins
- Check transactions successful?
- Make Coffee

"""
# Resources
from main import MENU, resources


def report():
    print("Water: {}ml".format(Water))
    print("Milk: {}ml".format(Milk))
    print("Coffee: {}g".format(Coffee))
    print("Money: ${}".format(Money))


report()


which_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

if which_coffee == "espresso":
    Water -= 50
    Milk -= 0
    Coffee -= 18
    Money += 1.50
    print("I have enough resources, making you a coffee!")
elif which_coffee == "latte":
    Water -= 200
    Milk -= 150
    Coffee -= 24
    Money += 2.50
    print("I have enough resources, making you a coffee!")
elif which_coffee == "cappuccino":
    Water -= 250
    Milk -= 100
    Coffee -= 24
    Money += 3.00
    print("I have enough resources, making you a coffee!")
else:
    print("Sorry, not a valid option")


def check_resources(water, milk, coffee, money):
    if water < 0:
        print("Sorry, not enough water!")
    elif milk < 0:
        print("Sorry, not enough milk!")
    elif coffee < 0:
        print("Sorry, not enough coffee!")
    elif money < 0:
        print("Sorry, not enough money!")
    else:
        print("I have enough resources, making you a coffee!")