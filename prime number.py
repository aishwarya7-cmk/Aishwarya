def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage:
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    # If the number is not prime, print this message
    print(f"{num} is not a prime number.")
    
# Addition of prime numbers in a given range
prime_sum = 0
for i in range(2, num + 1):
    if is_prime(i):
        prime_sum += i
print(f"Sum of prime numbers from 2 to {num} is {prime_sum}.")