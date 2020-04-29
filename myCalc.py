num1 = int(input("Enter the first number: "))

x = input()
while x != "+" or "-" or "*" or "/":
    print("Input Incorrect")
    x = input()
    if x == "+" or "-" or "*" or "/":
        break

num2 = int(input("Enter the second number: "))

def operations(x): # example of function
    if x == "+":
        result = num1 + num2
        print(result)
    elif x == "-":
        result = num1 - num2
        print(result)
    elif x == "*":
        result = num1 * num2
        print(result)
    elif x == "/":
        result = num1 / num2
        print(result)
    else:
        print("Input Incorrect")

operations(x)
