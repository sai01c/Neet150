"""
https://leetcode.com/contest/weekly-contest-345/problems/maximum-number-of-moves-in-a-grid/
"""

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(r, c, prev):
            res = 0
            if (r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
                grid[r][c] <= prev
               ):
                return 0
            
            visit.add((r,c))
            res += 1
            directions = [[0,1], [-1,+1], [1,1]]
            
            temp = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                #we are getting max among the three directions because we only want to go in the max
                #direction.
                temp = max(temp, dfs(nr, nc, grid[r][c]))
                
            res += temp
            return res
        
        c = 0
        ans = 0

        for r in range(rows):
            ans = max(ans, dfs(r, 0, -1) - 1)

            
        return ans