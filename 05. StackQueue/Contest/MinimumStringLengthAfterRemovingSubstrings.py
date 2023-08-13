"""
https://leetcode.com/contest/weekly-contest-346/problems/minimum-string-length-after-removing-substrings/

"""

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == "B" and stack and stack[-1] == "A":
                stack.pop()
                
            elif char == "D" and stack and stack[-1] == "C":
                stack.pop()
            
            else:
                stack.append(char)
                
        return len(stack)