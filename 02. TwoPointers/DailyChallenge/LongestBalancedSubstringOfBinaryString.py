"""
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

tc - O(n)
sc - O(1)
"""

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        countzero = 0
        countone = 0
        prev = 1
        for right in range(len(s)):
            if (prev == 1 and s[right] == "0"): #that means we have to start our substring here
                #so set initial values here
                countzero = 0
                countone = 0
            
            if s[right] == "0": 
                countzero += 1
                prev = 0
            else:
                countone += 1
                prev = 1
            
            if countzero >= countone: #consider this example 001 answer is 2 
                #our countzero is 2, countone is 1 in this case
                res = max(res, 2*countone)
            
        return res