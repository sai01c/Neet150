"""
https://leetcode.com/problems/unique-paths/

Approach: this is again bottom to top dp. we come from end to begin
bottom row and last column will be 1 because we can only reach in a single way. (right, down)
we iterate from last second row and every time we create a row with 1. 
During iteration value will be sum of its next element and bottom element
after iterating that array, it will become the bottomrow for next time.

Tc: O(m*n)
Sc: O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        matrix = []
        for r in range(rows):
            temp = []
            for c in range(cols):
                temp.append(1)
            matrix.append(temp)
        
        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                matrix[r][c] = matrix[r+1][c] + matrix[r][c+1]
        
        return matrix[0][0]
