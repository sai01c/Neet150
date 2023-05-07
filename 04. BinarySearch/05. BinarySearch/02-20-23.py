"""
https://leetcode.com/problems/search-insert-position/

Approach: we will apply binary search because it is sorted array
and return left because we want actual position

Tc: O(logn)
Sc: O(1)

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        