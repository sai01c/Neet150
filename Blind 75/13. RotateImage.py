"""
https://leetcode.com/problems/rotate-image/

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

you are basically rotating the corners. 
first save the topLeft into a variable and start swapping the 4 corners. 
use the same while condition for doing it layer by layer. 
we use the for loops to iterate through the 4 directions. 
we are starting to see a pattern in matrices questions. 
while{
    for {
        swapping
    }
}

TC: 0(n^n)
SC: O(1)
"""


def rotateImage(matrix):
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    while left < right and top < bottom:
        # lc this solution is not working they recommended for i in range(right-left)
        # not sure what's the difference here
        for i in range(left, right):

            topLeft = matrix[top][left+i]

            matrix[top][left+i] = matrix[bottom-i][left]

            matrix[bottom-i][left] = matrix[bottom][right-i]

            matrix[bottom][right-i] = matrix[top+i][right]

            matrix[top+i][right] = topLeft

        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return matrix


print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
