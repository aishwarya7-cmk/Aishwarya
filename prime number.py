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