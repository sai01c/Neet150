"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

APPROACH: 2 sides are pacific, 2 are atlantic. 
from the pacific sides we start and we check what all can reach these sides
same with atlantic 2 sides, we start from the end of the grid to the middle and add to
atlantic. 
we use traditional dfs

TC: O(m*n) TODO
Sc: O(n)
"""

class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        pac = set()
        atl = set()
        
        def dfs(r, c, visit, prev):
            if (r not in range(rows) or c not in range(cols) or 
                (r,c) in visit or grid[r][c] < prev):
                return
            visit.add((r, c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, grid[r][c])
                
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pac, grid[r][c])
                    
        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, atl, grid[r][c])
                    
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r,c) in pac:
                    res.append([r, c])
        
        return res
    

class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        pac = set()
        atl = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(r, c, visit):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                x, y = q.popleft()
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if (
                    nr in range(rows) and 
                    nc in range(cols) and 
                    (nr,nc) not in visit and 
                    grid[nr][nc] >= grid[x][y]):
                        visit.add((nr, nc))
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    bfs(r, c, pac)
                    
        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    bfs(r, c, atl)
                    
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r,c) in pac:
                    res.append([r, c])
        
        return res
