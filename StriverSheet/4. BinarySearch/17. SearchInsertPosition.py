"""
https://leetcode.com/problems/search-insert-position/

Approach - do regular binary search but return left if we don't find the element because
we need to find the inserting position
 
tc - logn
sc - 1

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
        
        #inserting position
        return left
        