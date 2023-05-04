"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Approach - 

tc - 
sc - 

"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        total = 0
        for w in weights:
            total += w
        r = total
        
        while l <= r:
            m = (l + r) // 2
            temp = 0
            d = 1
            for w in weights:
                temp += w
                if temp > m:
                    temp = w
                    d += 1
                
            
            if d <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
            
                
        return res
        
        