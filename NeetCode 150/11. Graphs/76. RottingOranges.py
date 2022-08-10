"""

TC: O(m*n)
"""

import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1  # add fresh count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))  # get initial rotten to q

        while q and fresh > 0:  # adding fresh here because once we are done
            # rotting the fresh oranges we can return.
            # if we don't include fresh condition we might keep rotting other oranges.
            # including for loop because each iteration we can take all the rotten oranges
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
