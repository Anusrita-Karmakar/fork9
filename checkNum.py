import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Check if a single number is prime
num = int(input("Enter a number to check if it's prime: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# Print prime numbers in a range (1–100)
print("\nPrime numbers between 1 and 100:")
for i in range(2, 101):
    if is_prime(i):
        print(i, end=" ")
