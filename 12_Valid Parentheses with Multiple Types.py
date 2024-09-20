# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:31:35 2024

@author: venka
"""

def main(s):
     mapping={ ']':'[','}':'{',')':'(' }
     stack=[]
     
     for str in s:
         if str in mapping:
             if stack and stack[-1]==mapping[str]:
                 stack.pop()
             else:
                 return False
         else:
            stack.append(str)
     return not stack
            
            
# Test Cases
print(main("()"))      # Output: True
print(main("([)]"))    # Output: False
print(main("[{()}]"))  # Output: True
print(main(""))        # Output: True
print(main("{[}"))     # Output: False


userinput = input("Enter a string of parentheses: ")

print(main(userinput))


             
         
         