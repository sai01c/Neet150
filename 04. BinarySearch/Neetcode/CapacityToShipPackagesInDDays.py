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
        def helper(cap):
            day = 1
            total = 0
            for w in weights:
                total += w
                if total > cap: #only if weight exceeds we increase day 
                    day += 1
                    total = w
            return day <= days
                
        l = max(weights)
        r = sum(weights)
        ans = -1
        while l <= r:
            m = (l+r) // 2
            if helper(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
                
        
        