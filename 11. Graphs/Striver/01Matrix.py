"""
https://leetcode.com/problems/01-matrix/

Approach - if distance or something similar metrix always have BFS.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        visit = set()
        rows = len(mat)
        cols = len(mat[0])
        step = 0

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
                    
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if mat[r][c] == 0:
                    step = 0
                else:
                    mat[r][c] = step
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (
                        (nr, nc) not in visit and 
                        nr in range(rows) and
                        nc in range(cols)
                    ):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            step += 1
                    
        
        
        return mat