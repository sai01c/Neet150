"""
https://leetcode.com/problems/valid-word-square/

"""

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        mat = []
        rows = len(words)
        cols = 0
        for row in words:
            cols = max(cols, len(row))
        if rows != cols:
            return False
        
        for i in range(rows):
            temp = []
            for j in range(cols):
                if j < len(words[i]):
                    temp.append(words[i][j])
                else:
                    temp.append(' ')
            mat.append(temp)
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != mat[c][r]:
                    return False
        return True