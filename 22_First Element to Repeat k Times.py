# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:20:53 2024

@author: venka
"""

def first_element_to_repeat_k_times(arr, k):
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    for num in arr:
        if count[num] == k:
            return num

    return -1

# Test Cases
print(first_element_to_repeat_k_times([3, 1, 4, 4, 5, 2, 6, 1, 4], 2))  # Output: 1
print(first_element_to_repeat_k_times([2, 3, 4, 2, 2, 5, 5], 2))       # Output: 5
print(first_element_to_repeat_k_times([1, 1, 1, 1], 1))                 # Output: -1
print(first_element_to_repeat_k_times([10], 1))                          # Output: 10
print(first_element_to_repeat_k_times([6, 6, 6, 6, 7, 7, 8, 8, 8], 3))  # Output: 8

if __name__ == "__main__":
    # Taking input for the array and k
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))

    # Calling the function and printing the result
    result = first_element_to_repeat_k_times(arr, k)
    print(f"Output: {result}")