"""
https://leetcode.com/problems/shortest-bridge/
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = collections.deque()
        def dfs(r, c):
            if (r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
               grid[r][c] != 1):
                return
            visit.add((r, c))
            q.append((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)
        done = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    dfs(r,c)
                    done = True
                    if done: break
            if done: break
            
        res = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dr, dc in directions:
                    nr, nc = x+dr, y+dc
                    if (nr in range(rows) and nc in range(cols) and (nr,nc) not in visit):
                        if grid[nr][nc] == 1:
                            return res
                        visit.add((nr,nc))
                        q.append((nr,nc))
            res += 1
        return res-1
                    

        