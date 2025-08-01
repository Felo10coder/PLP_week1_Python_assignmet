# Simple Calculator

# Ask for input
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform operation
if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")

elif operation == "-":
    result = abs(first_number - second_number)
    print(f"{first_number} - {second_number} = {result}")

elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")

elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please enter one of: +, -, *, /")