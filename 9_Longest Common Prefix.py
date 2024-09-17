# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:30:39 2024

@author: venka
"""

class Solution:
    def lcp(self, wrds):  # lcp: longest common prefix, wrds: words
        if len(wrds) == 0:
            return ""
        
        sml_len = min(len(w) for w in wrds)  # sml_len: smallest length, w: word
        
        for i in range(sml_len):
            ch = wrds[0][i]  # ch: character
            for w in wrds:
                if w[i] != ch:
                    return wrds[0][:i]
        
        return wrds[0][:sml_len]

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    strs1 = ["flower", "flow", "flight"]
    print(f"Input: {strs1}")
    print(f"Output: {sol.lcp(strs1)}")  # Expected: "fl"
    print()
    
    # Test Case 2
    strs2 = ["dog", "racecar", "car"]
    print(f"Input: {strs2}")
    print(f"Output: {sol.lcp(strs2)}")  # Expected: ""
    print()
    
    # Test Case 3
    strs3 = ["apple", "ape", "april"]
    print(f"Input: {strs3}")
    print(f"Output: {sol.lcp(strs3)}")  # Expected: "ap"
    print()
    
    # Test Case 4
    strs4 = [""]
    print(f"Input: {strs4}")
    print(f"Output: {sol.lcp(strs4)}")  # Expected: ""
    print()
    
    # Test Case 5
    strs5 = ["alone"]
    print(f"Input: {strs5}")
    print(f"Output: {sol.lcp(strs5)}")  # Expected: "alone"
    print()

def main():
    sol = Solution()
    
    user_input = input("Enter a list of strings separated by spaces: ").strip()
    
    if user_input:
        strs = user_input.split()
    else:
        strs = []
    
    result = sol.lcp(strs)

    print("Longest Common Prefix:", result)

if __name__ == '__main__':
    main()