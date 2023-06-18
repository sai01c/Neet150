"""
https://leetcode.com/problems/maximal-square/
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dic = {}

        def backtrack(r, c):
            if r >= rows or c >= cols:
                return 0
            if (r, c) in dic:
                return dic[(r, c)]
            
            right = backtrack(r + 1, c)
            bottom = backtrack(r, c + 1)
            diagonal = backtrack(r + 1, c + 1)
            
            if matrix[r][c] == "1":
                dic[(r, c)] = 1 + min(right, bottom, diagonal)
            else:
                dic[(r,c)] = 0
                
            return dic[(r, c)]

        backtrack(0, 0)
        maxLen = max(dic.values())

        return maxLen ** 2
