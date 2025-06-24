def factorial_number(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    fact= 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact

while True:
    n = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {n} is: {factorial_number(n)}")
    again = input("Do you want to calculate another factorial? (yes/no): ").lower().strip()
    if again == 'no':
        print("Ending the program.")
        break
    