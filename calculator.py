# Functions for the operators

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Store the functions in a dict

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Take inputs
num1 = float(input("What's the first number? "))

# Loop through the dict to select symbol
for symbol in operations:
    print(symbol)

operations_symbol = input("Pick an operator from above ")

calculation_function = operations[operations_symbol]

num2 = float(input("What's the second number? "))

answer = calculation_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")