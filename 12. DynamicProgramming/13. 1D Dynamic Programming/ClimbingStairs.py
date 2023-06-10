"""
https://leetcode.com/problems/climbing-stairs/

Approach: for n more than 3, number of steps is sum of n-1 + n-2
because we can only make 1 or 2 steps each time.
Now, we need to use memoization or tabulation to optimize this
this is basically fibonacci problem

Tc: O(n) 
Sc: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        #these are basically the last two values
        #For n = 3, it is sum of n-1 and n-2
        #so calculate n-1 and n-2 values
        #for n = 3 , previous value is n=2 which is 2
        #and previous2 value is n=1 which is 1
        prev = 2 
        prev2 = 1
           
        for i in range(3, n+1):
            curr = prev2 + prev #calculate for this value of n
            prev2 = prev #shifting the pointers forward
            prev = curr 
            #for next iteration, previous will be curr and previous2 will be previous.
            #shift the previous2 first
        return curr
    
#this is tabulation where we store the values in an array

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
           
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]