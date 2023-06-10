"""
https://leetcode.com/problems/unique-paths/

Approach: this is again bottom to top dp. we come from end to begin
bottom row and last column will be 1 because we can only reach in a single way. (right, down)
we iterate from last second row and every time we create a row with 1. 
During iteration value will be sum of its next element and bottom element
after iterating that array, it will become the bottomrow for next time.

Tc: O(m*n)
Sc: O(n)
"""

def uniquePaths(m, n):
    rows , cols = m, n
    bottomRow = [1] * n

    for r in range(rows-1):
        newRow = [1] * cols
        for c in range(cols-2, -1, -1):
            newRow[c] = newRow[c+1] + bottomRow[c]
        bottomRow = newRow

    return bottomRow[0]