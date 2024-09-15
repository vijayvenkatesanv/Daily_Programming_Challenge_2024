# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:32:54 2024

@author: venka
"""

def trap(height):
    if not height or len(height) < 3:
        return 0  

    n = len(height)
    
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill the left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    
    # Fill the right_max array
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    water_trapped = 0
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - height[i]
    
    return water_trapped

# Test cases
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
print(trap([4, 2, 0, 3, 2, 5]))  # Output: 9
print(trap([1, 1, 1]))  # Output: 0
print(trap([5]))  # Output: 0
print(trap([2, 0, 2]))  # Output: 2

if __name__ == "__main__":
    user_input = input("Enter the heights separated by spaces: ")
    height = list(map(int, user_input.split()))
    
    result = trap(height)
    print(f"Total water trapped: {result}")