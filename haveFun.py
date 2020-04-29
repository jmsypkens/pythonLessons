num1 = int(input())
x = input()
num2 = int(input())

def operations(x):
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
