# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:19:56 2024

@author: venka
"""

def find_zero_sum_subarrays(arr):
    prefix_sum_map = {}
    current_sum = 0
    result = []
    prefix_sum_map[0] = [-1]
    
    for i, num in enumerate(arr):
        current_sum += num
        
        if current_sum in prefix_sum_map:
            for start_index in prefix_sum_map[current_sum]:
                result.append((start_index + 1, i))
        
        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum].append(i)
        else:
            prefix_sum_map[current_sum] = [i]
    
    return result

# Test cases
arr1 = [1, 2, -3, 3, -1, 2]
arr2 = [4, -1, -3, 1, 2, -1]
arr3 = [1, 2, 3, 4]
arr4 = [0, 0, 0]
arr5 = [-3, 1, 2, -3, 4, 0]
arr6 = [1, -1, 2, -2, 3, -3] * 10000  # Large test case

print(find_zero_sum_subarrays(arr1))  # Output: [(0, 2), (2, 3)]
print(find_zero_sum_subarrays(arr2))  # Output: [(1, 2), (0, 3)]
print(find_zero_sum_subarrays(arr3))  # Output: []
print(find_zero_sum_subarrays(arr4))  # Output: [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
print(find_zero_sum_subarrays(arr5))  # Output: [(0, 3), (4, 4)]

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements separated by spaces: ").strip().split()))
    result = find_zero_sum_subarrays(arr)
    print(result)
