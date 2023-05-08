"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Approach: here, we have to find capacity which will be between two intervals. 
minCap, maxCap and it is sorted between these two, so binary search
have generic binary search but every time after computing mid, to shift pointers
we will calculate did our maxCap is satisfying the days they gave based on that we
shift our pointers

- this is similar to koko eating banana's

Tc: O(n logn) sc - O(1)

"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
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
        
        