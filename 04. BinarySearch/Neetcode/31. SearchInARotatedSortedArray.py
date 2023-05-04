"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Pattern: Binary Search as it is sorted
First, as it is rotated, we need to find the minimum of the array by using binary search. 
Next, using that minimum element, assign the left and right pointers and apply binary search

TC: O(logn)
Sc: O(1)
"""


def search(nums, target):
    left = 0
    right = len(nums)-1

    #first find the least element
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid+1
    least = left
    right = len(nums) - 1
    left = 0

    #based on least element shift the pointer's.
    if target <= nums[right] and target >= nums[least]:
        left = least
    else:
        right = least - 1

    #find the target element in the updated pointers
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid-1
        elif target > nums[mid]:
            left = mid+1
    #target is not there in our array
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))
