import math

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

def power(a, b):
    return a ** b

print("Welcome to the Calculator! You can perform the following operations:")
while True:
     print("\nCalculator Menu:")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")
     print("5. Modulus")
     print("6. Power")
     print("7. root square")
     print("8. Exit")
        
     choice = input("Enter your choice (1-8): ")
        
     if choice == '8':
         print("Exiting the calculator.")
         break
        
     if choice in ['1', '2', '3', '4', '5', '6', '7']:
         try:
             if choice == '7':
                 a = float(input("Enter number to find the square root: "))
                 if a < 0:
                     print("Error: Cannot calculate square root of a negative number.")
                     continue
             else:
                 a = float(input("Enter first number: "))
                 b = float(input("Enter second number: "))
         except ValueError:
             print("Invalid input. Please enter numeric values.")
             continue
            
         if choice == '1':
             result = sum(a, b)
         elif choice == '2':
             result = subtract(a, b)
         elif choice == '3':
             result = multiply(a, b)
         elif choice == '4':
             result = divide(a, b)
         elif choice == '5':
             result = modulus(a, b)
         elif choice == '6':
             result = power(a, b)
         elif choice == '7':
             result = math.sqrt(a)
         else:
             print("Invalid choice. Please select a valid option.")
             continue

         print(f"The result is: {result}")