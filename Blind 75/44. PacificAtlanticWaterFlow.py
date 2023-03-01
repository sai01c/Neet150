"""
https://leetcode.com/problems/pacific-atlantic-water-flow/


APPROACH: we use the generic dfs approach
we add the condition if height[r][c] < previous height

we apply the dfs approach on all four sides. and then check the two sets for any 
common points

TC: O(m*n)
"""


def pacatl(graph):
    rows = len(graph)
    cols = len(graph[0])
    pac = set()
    atl = set()

    def dfs(r, c, visit, prevHeight):

        if (r < 0
            or c < 0
            or r == rows
            or c == cols
                or graph[r][c] < prevHeight
                or (r, c) in visit):
            return

        visit.add((r, c))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            dfs(r+dr, c+dc, visit, graph[r][c])

    for r in range(rows):
        dfs(r, 0, pac, graph[r][0])
        dfs(r, cols-1, atl, graph[r][cols-1])

    for c in range(cols):
        dfs(0, c, pac, graph[0][c])
        dfs(rows-1, c, atl, graph[rows-1][c])

    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacatl(heights))
