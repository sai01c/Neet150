"""
https://leetcode.com/problems/spiral-matrix-ii/

"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows, cols = n, n
        l = 0
        r = cols - 1
        
        t = 0
        b = rows - 1
        val = 1
        
        mat = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            mat.append(row)
        
        
        while l <= r and t <= b:
            for i in range(l, r+1):
                mat[t][i] = val
                val += 1
            t += 1
                
            for i in range(t, b+1):
                mat[i][r] = val
                val += 1
            r -= 1
                
            for i in range(r, l-1, -1):
                mat[b][i] = val
                val += 1
            b -= 1
                
            for i in range(b, t-1, -1):
                mat[i][l] = val
                val += 1
            l += 1
            
        return mat