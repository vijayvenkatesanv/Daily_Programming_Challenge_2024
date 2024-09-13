# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:09:57 2024

@author: venka
"""

def leader(num,m):
    leader=[]
    high=num[m-1]  #high ---> biggest element from right
    leader.append(high)
    for i in range(m-2,-1,-1): # loop in reverse 
        if num[i]>=high:
            leader.append(num[i])
            high=num[i]
    leader.reverse()
    return leader
    
# Test Cases
print("Test Case 1:", leader([1, 2, 3, 4, 0], 5))  # Output: [4, 0]
print("Test Case 2:", leader([7, 10, 4, 10, 6, 5, 2], 7))  # Output: [10, 6, 5, 2]
print("Test Case 3:", leader([5], 1))  # Output: [5]
print("Test Case 4:", leader([100, 50, 20, 10], 4))  # Output: [100, 50, 20, 10]
print("Test Case 5:", leader(list(range(1, 1000001)), 1000000))  # Output: [1000000]

m = int(input("Enter the size of the first array (m): "))
num = list(map(int, input(f"Enter {m} elements for the first array: ").split()))

print("Leaders List:" , leader(num,m))