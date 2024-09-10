# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:06:51 2024

@author: venka
"""

def missing_number(arr):
    n=len(arr)+1
    totalsum=n*(n+1)//2  # Sum of first n natural numbers
    arr_sum=sum(arr)
    return totalsum - arr_sum  # This difference is the missing number
 
# Test cases
print(missing_number([1, 2, 4, 5]))  # Output: 3
print(missing_number([2, 3, 4, 5]))  # Output: 1
print(missing_number([1, 2, 3, 4]))  # Output: 5
print(missing_number([1]))           # Output: 2
print(missing_number(list(range(1, 1000000))))  # Output: 1000000    
 