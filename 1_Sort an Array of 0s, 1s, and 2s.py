# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:01:32 2024

@author: venka
"""
#day_1
def sort_array(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
#Dutch National Flag Algorithm
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
             
    return arr

# Test Cases
print(sort_array([0, 1, 2, 1, 0, 2, 1, 0]))  # Output: [0, 0, 0, 1, 1, 1, 2, 2]
print(sort_array([2, 2, 2, 2]))              # Output: [2, 2, 2, 2]
print(sort_array([0, 0, 0, 0]))              # Output: [0, 0, 0, 0]
print(sort_array([1, 1, 1, 1]))              # Output: [1, 1, 1, 1]
print(sort_array([2, 0, 1]))                 # Output: [0, 1, 2]
print(sort_array([]))                        # Output: []
