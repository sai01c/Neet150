"""
https://leetcode.com/problems/minimum-path-sum/

Approach - this is dynamic programming problem. I have done similar pattern before unique paths.
we have to iterate in reverse direction. 
First iterate through last row and last column seperately and add the next element.
now iterate both row and columns excluding last row and last columns
For each element calculate sum of this element plus right element or bottom element. Take the min of these two.

Tc: O(n^2)
Sc: O(1) no additional space

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid) #basic step for any matrix based question
        cols = len(grid[0])
        
        for c in range(cols-2, -1, -1): #modify last row elements by adding its right element
            grid[-1][c] += grid[-1][c+1]
            
        for r in range(rows-2, -1, -1): #modify last column elements by adding its bottom element
            grid[r][-1] += grid[r+1][-1]
            
        for r in range(rows-2, -1, -1): #add left and bottom element and take min of those two.
            for c in range(cols-2, -1, -1):
                grid[r][c] = min( 
                                grid[r][c] + grid[r][c+1], 
                                grid[r][c] + grid[r+1][c]
                                )
                
        
        return grid[0][0] #first element will be the min path
            