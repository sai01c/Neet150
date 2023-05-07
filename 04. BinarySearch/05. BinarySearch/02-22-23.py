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
        minCap = max(weights)
        maxCap = 0
        ans = float('inf')
        for w in weights:
            maxCap += w
        while minCap <= maxCap:
            midCap = (minCap + maxCap) // 2
            #this is the tricky part - we calculate day based on the midCap
            total = 0
            day = 1
            for w in weights:
                total += w
                if total > midCap: #this means our midCap can't satisfy this we move on to next ship
                    total = w
                    day += 1
            
            if day <= days:
                maxCap = midCap - 1
                ans = min(ans, midCap)
            else:
                minCap = midCap + 1
        return ans