"""
https://leetcode.com/problems/gas-station/

Approach - if sum of gas we have is less than sum of cost then return -1 because no way we can
traverse if what we have is less.

tc
sc

"""

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost): return -1
        start = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:
                total = 0
                start = i + 1
        
        return start