def evaluate_expression(expression):
    # Replace ' ' (spaces) in the expression
    expression = expression.replace(" ", "")

    # Initialize the result and the sign
    result = 0
    sign = 1

    # Iterate through the expression
    i = 0
    while i < len(expression):
        # If the current character is a digit, extract the whole number
        if expression[i].isdigit():
            start = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            result += sign * float(expression[start:i])

        # If the current character is '+', set the sign to positive
        elif expression[i] == '+':
            sign = 1
            i += 1

        # If the current character is '-', set the sign to negative
        elif expression[i] == '-':
            sign = -1
            i += 1

    if result == 0:
        return True
    else:
        return False

def find_expression(n):
    flag = False
    if n <= 0:
        print("No solution")
        return

    stack = [(0, "", 1, 0)]

    while stack:
        current_sum, current_expression, current_num, depth = stack.pop()

        if current_num == n + 1:
            if evaluate_expression(current_expression):
                flag = True
                print(current_expression)  # Print without the leading '+'
                break
            else:
                continue

        stack.append((current_sum + current_num, current_expression + f"+{current_num}", current_num + 1, depth + 1))
        stack.append((current_sum - current_num, current_expression + f"-{current_num}", current_num + 1, depth + 1))
    
    if not flag:
        print("No solution")

try:
    n = int(input("Enter a number: "))
    find_expression(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
