
def display_menu():
    print("\n" + "="*40)
    print("         TERMINAL CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Power (**)")
    print("7. Exit")
    print("="*40)

def calculate(operation, num1, num2):
    if operation == 1:
        result = num1 + num2
        symbol = "+"
    elif operation == 2:
        result = num1 - num2
        symbol = "-"
    elif operation == 3:
        result = num1 * num2
        symbol = "*"
    elif operation == 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
        symbol = "/"
    elif operation == 5:
        if num2 == 0:
            print("Error: Modulo by zero is not allowed!")
            return
        result = num1 % num2
        symbol = "%"
    elif operation == 6:
        result = num1 ** num2
        symbol = "**"
    else:
        print("Invalid operation.")
        return

    print(f"\n{num1} {symbol} {num2} = {result}")


print("Welcome to the Terminal Calculator!")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input! Please enter a number between 1-7.")
        continue
    
    if choice == 7:
        print("\nThank you for using the Terminal Calculator!")
        print("Goodbye!")
        break
    
    if choice < 1 or choice > 7:
        print("Invalid choice! Please select a number between 1 and 7.")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        continue
    
    calculate(choice, num1, num2)
    
    while True:
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
        if continue_calc in ['y', 'yes']:
            break
        elif continue_calc in ['n', 'no']:
            print("\nThank you for using the Terminal Calculator!")
            print("Goodbye!")
            exit()
        else:
            print("Please enter 'y' for yes or 'n' for no.")
