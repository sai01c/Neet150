"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        dic = {}
        
        def dfs(r, c, prev):
            if (r,c,prev) in dic:
                return dic[(r,c, prev)]
            ans = 0
            maxi = 0
            if (r not in range(rows) or 
               c not in range(cols) or
                matrix[r][c] <= prev):
                return ans
            ans += 1
            directions = [[0,1], [0,-1], [1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                maxi = max(maxi, dfs(nr, nc, matrix[r][c]))
            ans += maxi
            dic[(r,c, prev)] = ans
            return ans
            
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))
        
        return res