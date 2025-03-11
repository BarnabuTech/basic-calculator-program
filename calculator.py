# This Basic Calculator Program for my PLP Python Programming Module.

def calculator():
    print("Welcome to the Basic Calculator!")
    
    # Getting the numbers and operation from the user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Performing the selected operation when if the user input the numbers and operations
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")

# Running the calculator
if __name__ == "__main__":
    calculator()