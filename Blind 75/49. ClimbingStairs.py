"""
https://leetcode.com/problems/climbing-stairs/

Approach: for n more than 3, number of steps is sum of n-1 + n-2
because we can only make 1 or 2 steps each time.
Now, we need to use memoization or tabulation to optimize this
this is basically fibonacci problem

Tc: O(n) 
Sc: O(1)
"""

def func(n):
    if n<= 3:
        return n
    prev2 = 2
    prev = 3
    for i in range(4, n+1):
        curr = prev + prev2
        prev2 = prev #shifting pointers always note down 
        #prev2 , prev,  curr - old
        # n/a  , prev2, prev - new
        prev = curr

    return curr