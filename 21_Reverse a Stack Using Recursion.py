# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:59:55 2024

@author: venka
"""

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)
        
# Test Case 1
stack = [3, 2, 1]
reverse_stack(stack)
print(stack)  # Output: [1, 2, 3]

# Test Case 2
stack = [5]
reverse_stack(stack)
print(stack)  # Output: [5]

# Test Case 3
stack = [-5, -10, -15]
reverse_stack(stack)
print(stack)  # Output: [-15, -10, -5]

# Test Case 4
stack = []
reverse_stack(stack)
print(stack)  # Output: []

# Test Case 5
stack = [3, 3, 3]
reverse_stack(stack)
print(stack)  # Output: [3, 3, 3]


# Function to take user input and reverse the stack
def main():
    stack = list(map(int, input("Enter the elements of the stack separated by spaces: ").split()))
    reverse_stack(stack)
    print("Reversed stack:", stack)

if __name__ == "__main__":
    main()
