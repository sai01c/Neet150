"""
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
"""

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dic = {}
        mod = 10**9 + 7
        
        def dfs(r, c, prev):
            ans = 0
            if (r,c,prev) in dic:
                return dic[(r,c,prev)]
            if (r not in range(rows) or
               c not in range(cols) or
               grid[r][c] <= prev):
                return ans
            ans += 1
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                ans += dfs(nr, nc, grid[r][c])
            dic[(r,c,prev)] = ans
            return ans
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c, float('-inf'))
        
        return res % mod
                