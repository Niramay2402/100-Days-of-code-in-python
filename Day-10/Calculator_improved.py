# getting the previous answer and perform another operations and also using Recursion
from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    print(logo)
    num1 = float(input("Enter Number1: "))

    for symbol in operations:
        print(symbol)

    ans = True

    while ans:
        operation_symbol = input("Pick a Operation from the above: ")
        num2 = float(input("Enter the next number: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        intAns = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation..? "
                       f"\nEnter anything else to end...")

        if intAns == 'y':
            num1 = answer
        elif intAns == 'n':
            ans = False
            calculator()
        else:
            print("Goodbye!")
            break


calculator()
