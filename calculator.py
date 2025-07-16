print("\nCalculator App - Task 1\n\n")
while True:
    # Taking the user input
    print("Enter the expression you want to be calculated (e.g., 3 + 5):")
    user_input = input("Expression: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        break

    # Processing user input
    input_list = user_input.split(" ")

    if len(input_list) != 3:
        print("Invalid format. Please enter in the form: number operator number (e.g., 5 + 3)")
        continue

    num1, operator, num2 = input_list

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
        else:
            print("Unsupported operator. Use +, -, *, /")
            continue

        print("Result:", result)

    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
    print("\n")