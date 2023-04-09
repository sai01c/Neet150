"""
https://leetcode.com/problems/number-of-enclaves/

Approach - this is similar to closed islands, surrounding regions etc
First cross the borders and mark the all connected 1 as 0 as these are not useful for us
Now next iterate through the matrix and find number of 1's.

Tc - O(m*n)
Sc - O(m*n)

"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #0 sea 1 land
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (
                r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
                grid[r][c] != 1
            ):
                return
            
            visit.add((r,c))
            grid[r][c] = 0 #mark as 0 
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)

        #traverse through all the border's and mark all these 1 as 0 as these are not useful                
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r, c)
                    
        res = 0
        #traverse through matrix and find number of 1's.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 1
                    
        return res