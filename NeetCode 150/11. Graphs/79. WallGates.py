"""
https://www.lintcode.com/problem/663/

Approach - 0 is gate, -1 is wall, inf is empty
First, we iterate over and add all gates. From these gates, we do 
BFS because intuition we need to find distance every iteration. From all the
gates we do bfs and for each iteration increase distance by 1. 
This is similar to level order traversal

Tc - O(n) visit all nodes once
Sc - O(n) queue
"""

def wallGates(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = collections.deque()
    visit = set()
    directions = [[0,1], [0,-1], [1,0], [-1,0]]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0: #add all gates to the queue
                q.append((r,c))
                visit.add((r,c))
    
    #traditional bfs
    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr in range(rows) and 
                    nc in range(cols) and 
                    (nr,nc) not in visit and
                    grid[nr][nc] != -1):
                    q.append((nr, nc))
                    visit.add((nr, nc))

            dist += 1
