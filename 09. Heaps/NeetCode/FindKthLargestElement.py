"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

"""

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * int(num))
        
        for i in range(k):
            val = -1 * heapq.heappop(heap)
            
        return str(val)