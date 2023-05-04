Input = [1, 2, 3, 4, 5, 6]
Output = [6, 5, 4, 3, 2, 1]

"""
First, assign two pointer's left and right. Swap left and right pointers. 
Increment left by 1. Decrement right by 1. 
Tc: O(n)
SC: O(1)
"""


def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        swap(nums, left, right)
        left += 1
        right -= 1
    return nums


def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp


print(reverse(Input))
#[6, 5, 4, 3, 2, 1]
