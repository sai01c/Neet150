"""
https://leetcode.com/problems/equal-row-and-column-pairs/
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        for row in grid:
            dic[tuple(row)] += 1
        
        cols = len(grid[0])
        rows = len(grid)
        res = 0
        
        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(grid[r][c])
            res += dic[tuple(temp)]
        
        return res
