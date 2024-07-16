def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mult(a,b):
    return a*b
while True:
    first = int(input("Enter the first number: "))
    while True:
        operation = input("Enter the type of operation(+,-,*,/): ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            break
        else:
            print("Please enter a valid operation.")

    second = int(input("Enter the second number:"))

    if operation == "+":
        print(first, operation, second, " = ",add(first,second))
    elif operation == "-":
        print(first, operation, second, " = ", sub(first,second))
    elif operation == "*":
        print(first, operation, second, " = ", mult(first,second))
    else:
        print(first, operation, second, " = ", div(first,second))
    
    
    rerun = input("Do you want to continue using the calculator? (y//n): ")
    if rerun == 'y'or rerun == 'Y':
        continue
    else:
        break
