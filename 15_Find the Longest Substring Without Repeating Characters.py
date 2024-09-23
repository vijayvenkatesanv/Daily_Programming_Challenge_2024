# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:39:30 2024

@author: venka
"""

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    max_len = 0
    start = 0
    
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)
    
    return max_len

print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3
print(length_of_longest_substring("abcdefgh"))  # Output: 8
print(length_of_longest_substring("a"))         # Output: 1

S = input("Enter a string: ")
print(length_of_longest_substring(S))

