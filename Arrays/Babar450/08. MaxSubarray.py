"""
iterate through the array and add elements to running sum. 
if running sum less than zero, then make it zero. 
"""

("https://leetcode.com/problems/maximum-subarray/")


def subarray(nums):
    run_sum = 0
    maxi = 0
    for num in nums:
        if run_sum < 0:
            run_sum = 0
        run_sum += num
        maxi = max(maxi, run_sum)
    return maxi


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = 6
print(subarray(nums))
