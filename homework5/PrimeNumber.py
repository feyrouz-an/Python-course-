def prime_number(n): 
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False    
    return True
while True: 
    n = int(input("Enter a number to check if it is prime: "))
    print(f"{n} is a prime number: {prime_number(n)}") 
    again = input("Do you want to check another number? (yes/no): ").lower().strip() 
    if again == 'no':
        print("ending the program.")
        break