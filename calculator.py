
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operation = input("Enter the operation (+ for addition, - for subtraction, * for multiplication, / for division): ")


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("The result is: ",result)
