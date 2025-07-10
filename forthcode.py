num = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    print("The sum of the two number is: ", num + num2)
elif operator == "-":
    print("The difference of the two number is: ", num - num2)
elif operator == "*":
    print("The product of the two number is: ", num * num2) 
elif operator == "/":
    if num2 != 0:
        print("The division of the two number is: ", num / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")    