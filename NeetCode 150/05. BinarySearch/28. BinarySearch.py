"""
https://leetcode.com/problems/binary-search/

Approach: approach is to divide the number of elements into half each iteration. 
use left and right pointers
calculate mid each iteration 
and shift the pointers based on left, right, mid

Tc: O(logn)
Sc: O(1) constant 
"""


def binary(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return -1

    return -1


print(binary([-1, 0, 3, 5, 9, 12], 9))
