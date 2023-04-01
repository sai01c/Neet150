"""

Approach: Multi source BFS



Tc: 
"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        direct = [[-1,0], [1,0], [0,1],[0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c))
        res = -1
        while q:
            x, y = q.popleft()
            res = grid[x][y]
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if (nx in range(rows) and 
                ny in range(cols) and 
                grid[nx][ny] == 0):
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx,ny))
                                
        return res - 1 if res > 1 else -1

        
        
