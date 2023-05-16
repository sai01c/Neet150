"""
https://leetcode.com/problems/find-k-closest-elements/

"""

class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            num = nums[i]
            heapq.heappush(heap, (abs(num-x), i))
        
        res = []
        for i in range((k)):
            val, ind = heapq.heappop(heap)
            res.append(nums[ind])
            
        return sorted(res)