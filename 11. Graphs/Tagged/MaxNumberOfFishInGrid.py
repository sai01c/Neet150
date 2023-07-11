"""
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

"""

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c, visit):
            res = 0
            if (r not in range(rows) or
               c not in range(cols) or
               (r, c) in visit or
                grid[r][c] == 0):
                return 0
            
            visit.add((r, c))
            res += grid[r][c]
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for dr, dc in directions:
                nr, nc = r + dr, c+dc
                res += dfs(nr, nc, visit)
            
            return res
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c, set()))
                
        return ans