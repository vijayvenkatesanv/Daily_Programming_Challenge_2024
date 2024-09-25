# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:37:36 2024

@author: venka
"""

def prime_factors(N):
    factors = []
    divisor = 2
    
    while N % divisor == 0:
        factors.append(divisor)
        N //= divisor
    
    divisor = 3
    while divisor * divisor <= N:
        while N % divisor == 0:
            factors.append(divisor)
            N //= divisor
        divisor += 2
    
    if N > 1:
        factors.append(N)
    
    return factors

# Test Cases
print(prime_factors(30))      # Output: [2, 3, 5]
print(prime_factors(49))      # Output: [7, 7]
print(prime_factors(19))      # Output: [19]
print(prime_factors(64))      # Output: [2, 2, 2, 2, 2, 2]
print(prime_factors(123456))  # Output: [2, 2, 2, 2, 2, 3, 643]

# User Input
N = int(input("Enter a number: "))
print(prime_factors(N))
257