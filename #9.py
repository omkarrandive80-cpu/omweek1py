#9. Write a program to create a function that takes two numbers and an operator as arguments and returns the result of the operation (+, -, *, /).

def calculate(num1, num2, operator):    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
print(calculate(4, 2, '+'))
print(calculate(4, 2, '-'))
print(calculate(4, 2, '*'))
print(calculate(4, 2, '/'))
