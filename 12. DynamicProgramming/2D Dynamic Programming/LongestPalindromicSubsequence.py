"""
https://leetcode.com/problems/longest-palindromic-subsequence/
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mat = []
        rows = len(s)
        cols = len(s)
        for r in range(rows):
            temp = []
            for c in range(cols):
                temp.append(0)
            mat.append(temp)
        s2 = s[::-1]
        
        for r in range(rows):
            for c in range(cols):
                if s[r] == s2[c]:
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
