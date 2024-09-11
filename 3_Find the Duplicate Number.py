# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:39:48 2024

@author: venka
"""

def duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

# Test Cases:
print(duplicate([1, 3, 4, 2, 2]))  # Output: 2
print(duplicate([3, 1, 3, 4, 2]))  # Output: 3
print(duplicate([1, 1]))  # Output: 1
print(duplicate([1, 4, 4, 2, 3]))  # Output: 4
print(duplicate([i for i in range(1, 100000)] + [50000]))  # Output: 50000
