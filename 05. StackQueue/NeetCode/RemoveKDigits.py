"""
https://leetcode.com/problems/remove-k-digits/

Approach - if we see a smaller value than prev values then pop the stack
if length of stack is more than what you wanted then take the first values
because stack will be continously increasing.

now convert the stack to int 

tc - n
sc - n
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while stack and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(char)
        
        remain = len(stack) - k #continously increasing 
        stack = stack[:remain]
        
        res = "".join(stack)

        if res != "":
            return str(int(res))
        else:
            return "0"