def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")


def calculate():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        operator = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operator = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operator = "*"
    elif choice == '4':
        try:
            result = divide(num1, num2)
            operator = "/"
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid choice.")
        return

    print(f"{num1} {operator} {num2} = {result}")


calculate()
