"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Approach: take the first value and last value and run binary search 
shift the pointers by count function
which return number of elements in the matrix less than mid. 
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            count = self.count(matrix, k, mid)

            if (count < k):
                left = mid + 1
            else:
                right = mid

        return left

    def count(self, matrix, k, mid):
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (matrix[r][c] <= mid):
                    res += 1
        return res

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            heapq.heappush(heap, (matrix[r][0], r, 0))
        
        for i in range(k):
            ele, r, c = heapq.heappop(heap)
            
            if c+1 < cols:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        
        return ele