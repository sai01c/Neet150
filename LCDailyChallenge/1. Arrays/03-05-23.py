"""
https://leetcode.com/problems/pass-the-pillow/

Approach: first calculate the time to complete 1 pass
now divide the total time by time for one round
based on dividend we know if it is straight or reverse
use remainder to find the number

Tc: O(1) no loop
Sc: O(1) 
"""
import collections


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        timeToEnd = n - 1
        dividend = time // timeToEnd
        remain = time % timeToEnd
        
        if dividend % 2 == 0:
            return remain + 1
        else:
            return n - remain
        
