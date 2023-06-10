"""
https://leetcode.com/problems/buildings-with-an-ocean-view/

"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(heights)):
            h = heights[i]
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack