"""
https://leetcode.com/problems/longest-common-subsequence/

Approach: write it down in matrix form for better understanding
we create a matrix with 1 extra row and column. now if the text1 == text2
then it will be 1 + diagonal element
else we try to check what is the max b/2 next element and bottom element

Tc: O(n^2)
Sc: O(n)

"""

def lcs(text1, text2):
    rows = len(text1)
    cols = len(text2)
    matrix = []
    for r in range(rows+1):
        row = []
        for c in range(cols+1):
            rows.append(c)
        matrix.append(row)
    print(matrix)

    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if text1[r] == text2[c]:
                matrix[r][c] = 1 + matrix[r+1][c+1]
            else:
                matrix[r][c] = max(matrix[r+1][c], matrix[r][c+1])
    
    return matrix[0][0]