# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:20:41 2024

@author: venka
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l + 1:r]
        
        res = ""
        for i in range(len(s)):
            res = max(res, expand(i, i), expand(i, i + 1), key=len)
        return res

# Test Cases
sol = Solution()
print(sol.longestPalindrome("babad"))  # "bab"
print(sol.longestPalindrome("cbbd"))   # "bb"
print(sol.longestPalindrome("a"))      # "a"
print(sol.longestPalindrome("aaaa"))   # "aaaa"
print(sol.longestPalindrome("abc"))    # "a"


user_input = input("Enter a string: ")
print(f"Longest Palindromic Substring: {sol.longestPalindrome(user_input)}")
