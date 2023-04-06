"""
https://leetcode.com/problems/happy-number/

Approach - 


tc - 
sc - O(n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit: #if number if in visit that means its sum won't be 1
            visit.add(n) 
            n = self.helper(n) #get its sum of squares
            if n == 1:
                return True
        return False

    
    def helper(self, num): #to get the sum of squares of digits
        res = 0
        while num: 
            digit = num % 10 #get the last digit
            digit = digit * digit #square this digit
            res += digit #and add to output
            num = num // 10 #divide number by 10 and continue
        return res #return the sum 