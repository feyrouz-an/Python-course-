import math
def prime_number(n): 
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False    
    return True
N=int(input("enter a number N: "))
limit=int(math.sqrt(N))
sum_of_primes = 0
for i in range (2,limit + 1):
    if prime_number(i):
        sum_of_primes += i
print(f"The sum of all prime numbers up to sqrt({N}) is: {sum_of_primes}")