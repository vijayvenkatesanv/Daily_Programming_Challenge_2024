# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:15:41 2024

@author: venka
"""

from collections import defaultdict

def countSubstringsWithKDistinct(s: str, k: int) -> int:
    def countAtMostKDistinct(s, k):
        left = 0
        count = 0
        char_freq = defaultdict(int)
        
        for right in range(len(s)):
            char_freq[s[right]] += 1
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1
            count += right - left + 1
        return count
    
    return countAtMostKDistinct(s, k) - countAtMostKDistinct(s, k-1)

print(countSubstringsWithKDistinct("pqpqs", 2))  # Output: 7
print(countSubstringsWithKDistinct("aabacbebebe", 3))  # Output: 10
print(countSubstringsWithKDistinct("a", 1))  # Output: 1
print(countSubstringsWithKDistinct("abc", 3))  # Output: 1
print(countSubstringsWithKDistinct("abc", 2))  # Output: 2

s = input("Enter a string: ")
k = int(input("Enter the value of k: "))
result = countSubstringsWithKDistinct(s, k)
print(f"The number of substrings with exactly {k} distinct characters is: {result}")
