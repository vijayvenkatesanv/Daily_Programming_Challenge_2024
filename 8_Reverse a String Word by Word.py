# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:26:14 2024

@author: venka
"""

def reverseWords(s: str) -> str:
    words = s.split()
    
    reversed_words = words[::-1]
    
    result = " ".join(reversed_words)
    
    return result

# Test cases
print(reverseWords("the sky is blue"))       # Output: "blue is sky the"
print(reverseWords("  hello world  "))       # Output: "world hello"
print(reverseWords("a good   example"))      # Output: "example good a"
print(reverseWords("    "))                  # Output: ""
print(reverseWords("word"))                  # Output: "word"

user_input = input("Enter a string: ")
print("Reversed words:", reverseWords(user_input))