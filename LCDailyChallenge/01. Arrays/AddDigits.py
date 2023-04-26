"""
https://leetcode.com/problems/add-digits/

approach - add two numbers and see the result. you will notice to see a pattern
45 sum is 9 
36 sum is 9
81 sum is 9
23 sum is 5
41 sum is 5

if a number is divisible by 9 then sum is 9
if not remainder when divided by 9

"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9