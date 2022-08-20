"""
https://leetcode.com/problems/set-matrix-zeroes/

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

First, we need to iterate through the row and column to find the element which is equal to zero. 
Add that particular row and column to our sets. 
Now, again iterate through the row and column and mark them as zero if they are there in our lists. 

TC: O(m*n) two for loops
Sc: O(n) using set
"""


def matrixZero(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zeroRow = set()
    zeroCol = set()
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zeroRow.add(r)
                zeroCol.add(c)
    for r in range(m):
        for c in range(n):
            if r in zeroRow:
                matrix[r][c] = 0
            if c in zeroCol:
                matrix[r][c] = 0

    return matrix


print(matrixZero([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
