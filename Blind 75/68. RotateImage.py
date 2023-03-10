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


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        while left < right:
            for i in range(right- left):
                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft
            #after for loop, out outer boundary will be changed, now we want to increment pointers
            # to go into the inner layer. 
            # let us say for 4*4 matrix. After this for loop inside 2*2 will still be in original state
            # after we increase the pointers and do the for loop again we change inside 2*2 matrix    
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            
    


print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
