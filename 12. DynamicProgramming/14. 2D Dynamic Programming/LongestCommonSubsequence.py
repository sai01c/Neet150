"""
https://leetcode.com/problems/longest-common-subsequence/

Approach: write it down in matrix form for better understanding
we create a matrix with 1 extra row and column. now if the text1 == text2
then it will be 1 + diagonal element
else we try to check what is the max b/2 next element and bottom element

Tc: O(n^2)
Sc: O(n)

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = []
        rows = len(text1)
        cols = len(text2)
        for r in range(rows):
            temp = []
            for c in range(cols):
                temp.append(0)
            mat.append(temp)
        
        for r in range(rows):
            for c in range(cols):
                if text1[r] == text2[c]:
                    if r - 1 >= 0 and c-1 >= 0:
                        mat[r][c] = 1 + mat[r-1][c-1]
                    else:
                        mat[r][c] = 1
                else:
                    if r-1 >= 0 and c-1 >= 0:
                        mat[r][c] = max(mat[r][c-1], mat[r-1][c])
                    elif r-1 >= 0:
                        mat[r][c] = max(mat[r-1][c], 0)
                    elif c-1 >= 0:
                        mat[r][c] = max(mat[r][c-1], 0)
        
        return mat[rows-1][cols-1]
