number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
operator= input("Enter the operator: ")
if operator == "+":
    result=number1+number2
    print(f" {number1} + {number2} = {result}")
elif operator == "-":
    result=number1-number2
    print(f" {number1} - {number2} = {result}")
elif operator == "*":
    result=number1*number2
    print(f" {number1} * {number2} = {result}")
elif operator == "/":
    try:
        result=number1/number2
        print(f" {number1} / {number2} = {result}")
    except ZeroDivisionError:
        print(" It can't divide by zero")
else:
    print("Invalid operator")
