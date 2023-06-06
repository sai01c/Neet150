"""
https://leetcode.com/problems/combination-sum-ii/

Approach - this is similar to combination sum but diff is that numbers are not unique. 
we can't chose same number and we have to find unique combinations.

Tc - 2 ** len(nums)
sc - n + 2**len(nums)

"""


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() #sort the array first

        def backtrack(i, total, subset):
            if total == target:
                res.append(subset)
                return
            
            if i >= len(nums) or total > target:
                return
            
            #first case - add element
            subset.append(nums[i])
            total += nums[i]
            backtrack(i+1, total, subset)

            #second case - don't add element
            subset.pop()
            total -= nums[i]
            #we are doing this at the second case because we want to make sure
            #this will not contain any of the repeating element
            while i+1 < len(nums) and nums[i] == nums[i+1]: #if same element shift the pointer
                i += 1
            backtrack(i+1, total, subset)

        backtrack(0, 0, [])
        return res