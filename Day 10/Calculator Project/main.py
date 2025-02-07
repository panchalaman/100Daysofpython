from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {"+" : add, "-": subtract, "*": multiply, "/": divide}
should_continue= True
restart = True
while restart:
    result = 0
    num1= float(input("Type the first number: "))
    while should_continue:
        for operator in operations:
            print(operator)
        op = input("Choose the operator from above: ")
        num2= float(input("Type the second number: "))
        if op in operations:
            result= operations[op](num1, num2)
            print(f"{num1} {op} {num2} = {result}")
        further = input(f"Would you like to continue with {result}, y or n")
        if further == "y":
            num1 = result
        else:
            should_continue= False
            print("\n" * 20)
            restart = True
