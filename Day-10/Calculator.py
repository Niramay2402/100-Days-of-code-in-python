from art import logo

print(logo)


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

num1 = int(input("Enter Number1: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick a Operation from the above: ")

num2 = int(input("Enter Number2: "))

function = operations[operation_symbol]
print(f" \n {num1} {operation_symbol} {num2} = {function(num1, num2)}")

