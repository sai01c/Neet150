"""
https://leetcode.com/problems/as-far-from-land-as-possible/

"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c,0))
                    visit.add((r,c))
        res = 0
        while q:
            for i in range(len(q)):
                r, c, curr = q.popleft()
                res = max(res, curr)
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (
                        nr in range(rows) and
                       nc in range(cols) and
                    (nr, nc) not in visit and
                    grid[nr][nc] == 0
                    ):
        
                        q.append((nr, nc, curr+1))
                        visit.add((nr, nc))
        if res: return res
        return -1
                        