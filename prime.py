import random

x = random.randint(0,100)

def check_prime(x):
    if x < 2: 
        return False
    for i in range (2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

print(x, check_prime(x))