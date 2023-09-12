"""
https://leetcode.com/problems/island-perimeter/

Apple
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        1 -> land
        0 -> water
        """
        rows = len(grid)
        cols = len(grid[0])
        land = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land.add((r, c))
        res = 0
        for r,c in land:
            temp = 0
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr, nc) not in land:
                    temp += 1
            res += temp
        
        return res
        