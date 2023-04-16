"""
https://leetcode.com/problems/two-furthest-houses-with-different-colors/

Approach - farthest distance can only be with first or last node
so for every node calculate dist b/w first, last node and curr node.

tc - n
sc - 1
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        first = 0
        last = len(colors) - 1
        
        if colors[first] != colors[last]:
            #if they differ, that's the max possible distance.
            return abs(first - last)
        
        for i in range(len(colors)):
            #every iteration compare with first, last houses
            #because farthest dist will be with first, last houses
            if colors[i] != colors[first]:
                maxi = abs(i - first)
                ans = max(ans, maxi)
                
            if colors[i] != colors[last]:
                maxi = abs(i - last)
                ans = max(ans, maxi)
            
                    
        return ans
                
                
        