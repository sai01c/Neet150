"""
https://leetcode.com/problems/search-a-2d-matrix/

Explanation: first we need to find the row using binary search approach, then find the element in that 
row using binary search 

Tc: O(log(m) + log(n))
Sc: 1
"""


def search2dMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    t = 0
    b = rows - 1
    while t <= b:
        m = (t+b) // 2
        if target < matrix[m][0]:
            b = m - 1
        elif target > matrix[m][-1]:
            t = m + 1
        else:  # why use break statement here - this condition means element is in the row 'm'
            break
    midRow = (t+b)//2
    l = 0
    r = cols - 1
    while l <= r:
        m = (l+r)//2
        if target < matrix[midRow][m]:
            r = m - 1
        elif target > matrix[midRow][m]:
            l = m + 1
        else:
            return True
    return False


print(search2dMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(search2dMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
