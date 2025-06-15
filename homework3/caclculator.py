try:
    n1 = float(input("enter a number :"))
    n2 = float(input("enter a number :"))
    print("what operation do you want to perform ?")
    operation = input("enter + for addition, - for subtraction, * for multiplication, / for division, % for modulo :")
    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2    
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        result = n1 / n2
    elif operation == "%":
        result = n1 % n2
    else:
        result = "Error: Invalid operation selected."   
except Exception as e:
    result = f"An unexpected error occurred: {e}"
print("The result is:", result)