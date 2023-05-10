"""
https://leetcode.com/problems/powx-n/

APPROACH: instead of doing x to the power of n, we can do x square to the power of n divided by 2
write on paper, this is basically same. 


TC: O(n)
SC: O(1)

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = self.helper(x, abs(n))
        if n > 0: 
            return temp
        else: #if negative number
            return (1 / temp)
    
    def helper(self, x, n):
        if x == 0: #base cases
            return 0
        if n == 0:
            return 1
        res = self.helper(x*x, n//2) #basically square number and divide n by 2
        if n % 2: #if odd number there will be an extra x
            res = res * x
        
        return res
