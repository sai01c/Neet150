"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

APPROACH: 2 sides are pacific, 2 are atlantic. 
from the pacific sides we start and we check what all can reach these sides
same with atlantic 2 sides, we start from the end of the grid to the middle and add to
atlantic. 
we use traditional dfs

TC: O(m*n)
Sc: 
"""

def pacAtl(heights):
    rows = len(heights)
    cols = len(heights[0])
    pac = set()
    atl = set()
    res = []

    def dfs(r, c, visit, prevHeight):
        if (r not in range(rows) or
            c not in range(cols) or 
            (r,c) in visit or
            heights[r][c] < prevHeight):
            return
        directions = [[0,1], [-1,0], [0,-1], [1,0]]
        visit.add((r,c))
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            dfs(nr, nc, visit, heights[r][c])
    #notice we are not removing from set.                                         
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols-1, atl, heights[r][cols-1])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows-1, c, atl, heights[rows-1][c])

    for r in range(rows):
        for c in range(cols):
            if (r,c) in atl and (r,c) in pac:
                res.append([r,c])

heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacAtl(heights))
