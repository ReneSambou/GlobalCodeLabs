## create a list with all the operations
def calculate(operation , num1 , num2 ):
    operation = operation.lower()
    if operation == "add":
        print(num1 + num2)
    elif operation == "multiply":
        print(num1*num2)
    elif operation == "divide":
        print(num1/num2)
    elif operation == "substract":
        print(num1 - num2)
    else:
        print("invalid input")
calculate("Multiply" , 1 , 2)
    