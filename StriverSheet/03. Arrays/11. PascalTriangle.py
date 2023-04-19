"""
https://leetcode.com/problems/pascals-triangle/

Approach - trick is we add padding to the previous array by adding 0's.

tc - O(n^2)
sc - O(n^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize with the first row containing only 1
        triangle = [[1]]
        
        # Generate the remaining rows
        for i in range(numRows - 1):
            # Add padding of 0s on both sides of the previous row
            prev_row_padded = [0] + triangle[-1] + [0]
            # Initialize a new row
            new_row = []
            
            # Iterate over each element in the previous row
            for j in range(len(triangle[-1]) + 1):
                # Add the sum of the adjacent elements to the new row
                element = prev_row_padded[j] + prev_row_padded[j+1]
                new_row.append(element)
            
            # Add the new row to the triangle
            triangle.append(new_row)
        
        # Return the result
        return triangle
 