"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Approach - we have to do it in O(n)
But, I am doing heap solution instead - klogn
First, heapify the nums and find the kth largest by popping 

tc - klogn
sc - n
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapfiy(nums) #n
            
        while(len(nums)) > k: #klogn
            heapq.heappop(nums)
        
        return nums[0]