"""
https://leetcode.com/problems/next-greater-element-ii/

Approach - only change is elements are in circular array - to handle this just append the original array to the original array i.e
[1,2,3] will be [1,2,3,1,2,3]
now follow next greatest element logic - monotonic stack to find
we are add ind, value to stack because we need to return the res in the same order of indices.

tc - n
sc - n
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        res = [-1] * len(nums)
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                val, ind = stack.pop()
                res[ind] = nums[i]
            
            stack.append((nums[i], i))
        
        return res[:n]
