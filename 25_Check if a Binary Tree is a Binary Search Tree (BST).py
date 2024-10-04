# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:39:17 2024

@author: venka
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))

def build_tree_from_list(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        current = queue.pop(0)

        if values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root


# Test cases
# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_bst(root1))  # Output: True

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(is_valid_bst(root2))  # Output: False

# Example 3
root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)
print(is_valid_bst(root3))  # Output: False

# Get user input for the binary tree
user_input = input("Enter the binary tree values in level-order (e.g., [2, 1, 3]): ")
user_input = user_input.strip()[1:-1]  # Remove brackets
values = [int(x) if x != 'null' else None for x in user_input.split(',')]

# Build the tree
root = build_tree_from_list(values)

# Check if the tree is a valid BST
result = is_valid_bst(root)
print("Is the binary tree a valid BST?", result)
