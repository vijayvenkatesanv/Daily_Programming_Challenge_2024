# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:36:53 2024

@author: venka
"""

def permute_unique(s: str):
    s = sorted(s)
    result = []
    used = [False] * len(s)
    
    def backtrack(path):
        if len(path) == len(s):
            result.append("".join(path))
            return
        
        for i in range(len(s)):
            if used[i]:
                continue

            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True
            backtrack(path + [s[i]])
            used[i] = False
    
    backtrack([])
    return result

# Test cases
print(permute_unique("abc"))   # ["abc", "acb", "bac", "bca", "cab", "cba"]
print(permute_unique("aab"))   # ["aab", "aba", "baa"]
print(permute_unique("aaa"))   # ["aaa"]
print(permute_unique("a"))     # ["a"]
print(permute_unique("abcd"))  # ["abcd", "abdc", "acbd", ..., "dcba"]

user_input = input("Enter a string: ")
permutations = permute_unique(user_input)
print("Unique permutations are:")
for p in permutations:
    print(p)
