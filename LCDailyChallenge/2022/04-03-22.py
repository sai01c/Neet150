"""
https://leetcode.com/problems/next-permutation/

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Find out the number which is the next greater using the same elements. 16789
First, iterate through the array in reverse direction and if the elements are in decreasing order like 6789
then reverse the elements to 19876. 
Next, among the elements that are reversed, check if any elements is the least among them and swap the first element to the greatest element. 
16879
"""


def next_permutation(nums):
    dec = len(nums) - 2
    while dec >= 0 and nums[dec] >= nums[dec+1]:
        dec -= 1
    reverse(nums, dec+1, len(nums)-1)
    if dec == -1:
        return nums
    next_num = dec + 1
    while next_num < len(nums) and nums[next_num] <= nums[dec]:
        next_num += 1
    swap(nums, dec, next_num)

    return nums


def reverse(nums, l, r):
    while l < r:
        swap(nums, l, r)
        l += 1
        r -= 1


def swap(nums, l, r):
    temp = nums[l]
    nums[l] = nums[r]
    nums[r] = temp


nums = [1, 2, 3]
print(next_permutation(nums))
nums = [3, 2, 1]
print(next_permutation(nums))
