"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q.append((0, 0))
        visit.add((0,0))
        res = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows-1 and c == cols-1:
                    return res
                directions = [[0,1],[0,-1],[1,0],[-1,0], [1,1],[-1,-1],[1,-1],[-1,1]]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and 
                       nc in range(cols) and 
                       (nr,nc) not in visit and
                       grid[nr][nc] == 0):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            res += 1
            
        return -1