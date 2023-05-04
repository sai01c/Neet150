
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach: we need to modify the array in place. sliding window concept but with diff logic. w
we inititate right at 0 and check if right == right + 1. out of the min of 2, count 
we append the right to the left index and increase left index.
end return left index as this will have the length of the new array

Tc: 
Sc: 
this problem is similar to string compression
"""

def removeDuplciates(nums):
    left = 0
    right = 0
    while right < len(nums):
        count += 1
        while right +  1 < len(nums) and nums[right] == nums[right+1]:
            count += 1
            right += 1
        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1
        right += 1
    return left

