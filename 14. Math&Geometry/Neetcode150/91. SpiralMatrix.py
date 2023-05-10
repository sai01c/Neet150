"""
https://leetcode.com/problems/spiral-matrix/

APPROACH: 
basically, we iterate through the each row and add to the res array. We decrease the respective
pointer every iteration.
We have to iterate through the matrix-2d. So, create 4 pointers left, right, top, bottom
For every while loop you'll iterate through the outermost layer elements
now to iterate through the outermost layer- create 4 loops in each direction
left to right, top to bottom and in the reverse directins.
after each direction increase the pointer by 1 


tc: O(m*n)
sc: O(n)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        top = 0
        bottom = rows - 1

        left = 0
        right = cols - 1

        while left <= right and top <= bottom:
            for c in range(left, right+1):
                res.append(matrix[top][c])
            top += 1

            for r in range(top, bottom+1):
                res.append(matrix[r][right])
            right -= 1
            #if a matrix is either single row or single column matrix we need to use this
            if not (left <= right and top <= bottom):  
                break

            for c in range(right, left-1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

            for r in range(bottom, top-1, -1):
                res.append(matrix[r][left])
            left += 1

        return res
