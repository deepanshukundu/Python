def add():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    result = x + y
    print(f"{x} + {y} = {result}")
    return result

def subtract():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    result = x - y
    print(f"{x} - {y} = {result}")
    return result

def multiply():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

def divide():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    result = x / y
    print(f"{x} / {y} = {result}")
    return result

def calculator():
    while True:
        try:
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. History")
            print("6. Quit")

            operation = int(input("Enter your choice: "))
            if operation in [1, 2, 3, 4]:
                if operation == 1:
                    add()
                elif operation == 2:
                    subtract()
                elif operation == 3:
                    multiply()
                elif operation == 4:
                    divide()
            elif operation == 5:
                print("\nHistory:")
                for calc in history:
                    print(calc)
            elif operation == 6:
                print("Quitting calculator...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

history = []
calculator()
