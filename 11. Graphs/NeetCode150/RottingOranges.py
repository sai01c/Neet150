"""
https://leetcode.com/problems/rotting-oranges/

Approach - do bfs because for every unit of time the surrounded cells get rotten. Intuition is
bfs when you write on paper

TC: O(m*n)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = collections.deque()
        fresh = 0
        time = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    fresh -= 1
                    grid[r][c] = 2
                if fresh == 0:
                    return time
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and
                       (nr,nc) not in visit and grid[nr][nc] == 1):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            time += 1
        
        if fresh == 0:
            return time
        return -1
                