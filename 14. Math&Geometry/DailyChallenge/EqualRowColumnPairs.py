"""
https://leetcode.com/problems/equal-row-and-column-pairs/

to get the column matrix, just you matrix[c][r]
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        for row in grid:
            dic[tuple(row)] += 1
        cols = []
        N = len(grid)
        for r in range(N):
            temp = []
            for c in range(N):
                temp.append(grid[c][r])
            cols.append(temp)
        res = 0
        for col in cols:
            if tuple(col) in dic:
                res += dic[tuple(col)]
        return res
                