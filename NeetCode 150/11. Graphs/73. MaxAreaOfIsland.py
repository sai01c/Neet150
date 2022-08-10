"""
Approach: we apply either bfs or dfs and add to visit if there's 1 
we extend the island if there's 1. we stop if all the four directions are 0
and return area

now apply starting at 0 index and check for max area. 

TC: O(m*n)

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            q, area = deque(), 1
            q.append((i, j))
            visited.add((i, j))

            while q:
                x, y = q.popleft()
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    r, c = x+dx, y+dy
                    if (r < 0 or c < 0
                        or r == ROWS or c == COLS
                            or grid[r][c] == 0 or (r, c) in visited):
                        continue

                    area += 1
                    q.append((r, c))
                    visited.add((r, c))

            return area

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(bfs(i, j), res)

        return res
