"""
https://leetcode.com/problems/number-of-closed-islands/

Approach - this problem is similar to surrounding regions. 
elements in 4 borders with 0 doesn't count because they can't be closed by 1. 
So, we will do dfs on 4 borders with these elements and continue to proceed with this island 
and mark them as 1 because they can never be closed by 1. 
If an element can be reached by these islands it also can't be closed. 

then, after all this do regular connected componenets algo to get the islands

Tc
Sc
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r,c) in visit or
                grid[r][c] != 0):
                return
            visit.add((r,c))
            grid[r][c] = 1 #mark this as 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)

        #traverse through entire matrix and mark all 0's as 1 because these 0 are not useful for us
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows-1] or c in [0, cols-1]:
                    dfs(r, c)
        
        print(grid)
        islands = 0
        #traverse through the matrix and find number of 0 islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        
        return islands