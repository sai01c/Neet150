"""
https://leetcode.com/problems/surrounded-regions/

APPROACH: first, we iterate through the 4 boundaries and check for O and we extend 
based on dfs. These we cannot capture so we mark them as T

Now, we iterate and check for any O (we can capture them) so mark them as X
Next, iterate and check for T, we can bring them back to O as we cannot capture them

TC: O(m*n)
"""


def sr(graph):

    rows = len(graph)
    cols = len(graph[0])

    def dfs(r, c):

        if (r < 0 or
            c < 0 or
            r == rows or
            c == cols or
                graph[r][c] != "O"):
            return
        graph[r][c] = "T"
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            dfs(r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if (graph[r][c] == "O" and
                    (r in [0, rows-1] or c in [0, cols-1])):
                dfs(r, c)

    for r in range(rows):
        for c in range(cols):
            if graph[r][c] == "O":  # we have not changed them to T
                graph[r][c] = "X"

    for r in range(rows):
        for c in range(cols):
            if graph[r][c] == "T":
                graph[r][c] = "O"

    return graph


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(sr(board))
