# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:02:15 2024

@author: venka
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagram_groups[sorted_string].append(string)
        
        return list(anagram_groups.values())

if __name__ == "__main__":
    # Test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
    
    # Test case 2
    strs = [""]
    print(solution.groupAnagrams(strs))
    
    # Test case 3
    strs = ["a"]
    print(solution.groupAnagrams(strs))
    
    # Test case 4
    strs = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
    print(solution.groupAnagrams(strs))
    
    # Test case 5
    strs = ["abc", "def", "ghi"]
    print(solution.groupAnagrams(strs))
    
    if __name__ == "__main__":
        strs = input("Enter strings separated by spaces: ").split()
    
    solution = Solution()
    grouped_anagrams = solution.groupAnagrams(strs)
    print(grouped_anagrams)
