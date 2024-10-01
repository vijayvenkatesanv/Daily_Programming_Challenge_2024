# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:23:45 2024

@author: venka
"""

from collections import deque

def sliding_window_maximum(arr, k):
    # Check if arr is empty
    if not arr:
        return []

    n = len(arr)
    result = []
    dq = deque()  # This will store indices of the array elements

    for i in range(n):
        # Remove indices from the front if they are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements from the back if they are smaller than the current element
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        # Add the current element index at the back of the deque
        dq.append(i)

        # Starting from i = k - 1, we will have valid windows, so start appending results
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Test Case 1
arr1 = [1, 5, 3, 2, 4, 6]
k1 = 3
print("Output for Test Case 1:", sliding_window_maximum(arr1, k1))  # Output: [5, 5, 4, 6]

# Test Case 2
arr2 = [1, 2, 3, 4]
k2 = 2
print("Output for Test Case 2:", sliding_window_maximum(arr2, k2))  # Output: [2, 3, 4]

# Test Case 3
arr3 = [7, 7, 7, 7]
k3 = 1
print("Output for Test Case 3:", sliding_window_maximum(arr3, k3))  # Output: [7, 7, 7, 7]

# Edge Case
arr4 = [5]
k4 = 1
print("Output for Edge Case:", sliding_window_maximum(arr4, k4))  # Output: [5]


# Take user input for the array and window size
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the window size k: "))

# Get and print the result
result = sliding_window_maximum(arr, k)
print("Output:", result)
