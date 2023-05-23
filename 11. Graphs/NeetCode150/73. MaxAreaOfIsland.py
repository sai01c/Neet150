"""
https://leetcode.com/problems/max-area-of-island/


Approach: we apply either bfs or dfs and add to visit if there's 1 
we extend the island if there's 1. we stop if all the four directions are 0
and return area

now apply starting at 0 index and check for max area. 

TC: O(m*n)
sc: 
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            area = 0 #for every cell initial area will be 0
            if (r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
               grid[r][c] == 0):
                return 0
            area += 1 #add 1 to area because this cell satisfied our conditions
            visit.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                area += dfs(nr, nc) #add neighbours area to the initial cell area
                
            return area
        res = 0 
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    res = max(res, dfs(r,c)) #get the highest area
                    
        return res

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            q, area = deque(), 1
            q.append((i, j))
            visited.add((i, j))

            while q:
                x, y = q.popleft()
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    r, c = x+dx, y+dy
                    if (r < 0 or c < 0
                        or r == ROWS or c == COLS
                            or grid[r][c] == 0 or (r, c) in visited):
                        continue

                    area += 1
                    q.append((r, c))
                    visited.add((r, c))

            return area

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(bfs(i, j), res)

        return res
