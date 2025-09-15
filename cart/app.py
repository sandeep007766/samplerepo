def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = 10
print(fibonacci(n))

# This is written by varun

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 7
print(f"Is {num} a prime number? {is_prime(num)}")

# Thankyou

# This is Madhuri
# I am a Cloud Engineer


# Line 2: After stashing changes
# Line 1: Performing git stashing
