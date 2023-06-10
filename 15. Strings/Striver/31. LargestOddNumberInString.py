"""
https://leetcode.com/problems/largest-odd-number-in-string/

approach

tc
sc

"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = {"1", "3", "5", "7", "9"} #create a set
        
        for i in range(len(num) - 1, -1, -1):
            digit = num[i]
            if digit in odd:
                return num[:i+1]
            
        
        return ""