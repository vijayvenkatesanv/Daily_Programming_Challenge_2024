

import math

def count_divisors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            count += 1
            if i != N // i:
                count += 1
    return count

# Test cases
print(count_divisors(18))  # Output: 6
print(count_divisors(29))  # Output: 2
print(count_divisors(100)) # Output: 9
print(count_divisors(1))   # Output: 1
print(count_divisors(997)) # Output: 2

# User input
N = int(input("Enter a number: "))
print(count_divisors(N))
