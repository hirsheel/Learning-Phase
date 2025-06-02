num1 = input("Enter Your First Number: "))
num2 = input("Enter Your Second Number: "))
op = input("Enter Your Operation; +, -, / (divide), *(multiply): ")
if (num1, num2) == int:
    num1 = int(num1)
    num2 = int(num2)
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("please enter valid operation Bruh!!!")
else:
    print("Give A Valid Number BRuh!!!")