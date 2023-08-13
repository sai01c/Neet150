"""
https://leetcode.com/problems/car-fleet/

Approach: we want to check if the elements reach target so we come in the reverse direction
sort the elements based on position. 
calculate time for each element.
we need to pop the smallest time as small will merge to large time
based on speeds, if s1 < s2 then they form a fleet
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            dic[p] = s
        
        sortedic = sorted(dic.items(), key = lambda x:x[0])
        
        stack = []
        for p, s in sortedic:
            t = (target - p) / s
            while stack and t >= stack[-1]:
                stack.pop()
        
            stack.append(t)
        
        return len(stack)
        
        