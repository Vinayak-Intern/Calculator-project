# Terminal Calculator

A simple terminal-based calculator written in Python.

## Features

- Basic arithmetic operations: +, -, *, /, %, **
- Menu-driven interface
- Error handling for invalid inputs and division by zero
- Support for decimal numbers

## Requirements

- Python 3.x

## Usage

Run the calculator:
```bash
python calculator.py
```

1. Select an operation from the menu (1-7)
2. Enter two numbers (integers or decimals)
3. View the result
4. Choose to continue or exit

## Operations

1. **Addition (+)** - Add two numbers
2. **Subtraction (-)** - Subtract second number from first
3. **Multiplication (*)** - Multiply two numbers
4. **Division (/)** - Divide first number by second (with zero-division protection)
5. **Modulo (%)** - Get remainder of division (with zero-division protection)
6. **Power (**)** - Raise first number to the power of second
7. **Exit** - Quit the calculator

## Example

```
Enter your choice : 1
Enter first number: 10.5
Enter second number: 5.2

10.5 + 5.2 = 15.7
```

## Error Handling

- Division by zero protection
- Invalid input validation
- Menu choice validation
```
