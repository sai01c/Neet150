"""
https://leetcode.com/problems/3sum/

Approach: first sort the numbers use the first number and iterate through the rest of the elements 
using two pointers. 
now repeat the same process for the rest of the first elements.

TC: O(n^2)
SC: O(n)

"""
def threeSum(nums):
    nums.sort()
    res = []
    for index, first_val in enumerate(nums):
        if index > 0 and nums[index] == nums[index-1]:  # to avoid duplicate values
            continue 
        left = index + 1
        right = len(nums) - 1
        while left < right:
            # always compute the equation after the while loop
            summ = first_val + nums[left] + nums[right]
            if summ < 0:
                left += 1
            elif summ > 0:
                right -= 1
            else:
                res.append([first_val, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:  # to avoid duplicates
                    left += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
