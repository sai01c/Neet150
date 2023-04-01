"""
https://leetcode.com/problems/rotting-oranges/

Approach - do bfs because for every unit of time the surrounded cells get rotten. Intuition is
bfs when you write on paper

TC: O(m*n)
"""

import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        fresh = 0
        time = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 #count of fresh cells
        
                if grid[r][c] == 2:
                    q.append((r, c)) #add all rotten cells to queue first
                    
        while q and fresh > 0: #why fresh condition - notice for the last cell after decreasing fresh by 1 
            #we still add that last rotten cell so q will continue for 1 more iteration so add fresh > 0 condiiton
            for i in range(len(q)):
                #for loop represents every unit of time
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and 
                            grid[nr][nc] == 1 and (nr, nc) not in visit):
                        grid[nr][nc] = 2 #rotten this cell
                        fresh -= 1 #decrease fresh 
                        q.append((nr, nc)) #append this rotten cell
                        visit.add((nr, nc))
            time += 1
            
        if fresh == 0: return time #only if fresh is 0
        return -1
        
        