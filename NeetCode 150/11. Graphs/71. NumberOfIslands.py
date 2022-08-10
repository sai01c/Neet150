"""

APPROACH: We can use DFS or BFS
Idea is either dfs or bfs if we have 1 add to visit and check in 4 directions if any of them is 1 we proceed. We quit if all the four sides have zeroes. 

Now we start at 0,0 and apply dfs or bfs. Now we check for the rest 

TC: O(m*n)
"""
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                x, y = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dx, dy in directions:
                    if (x + dx in range(row)) and (y + dy in range(col)) and (grid[x+dx][y+dy] == "1") and ((x+dx, y+dy) not in visit):
                        q.append((x+dx, y+dy))
                        visit.add((x+dx, y+dy))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
