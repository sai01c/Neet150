from cgitb import small


nums = [3, 9, 12, 16, 20]
K = 3
N = 4

"""
minimize the maximum difference
how do we get max difference- 20-2, 3+2= 18-5= 13

"""

# doubt


def minMaximize(nums):
    nums.sort()
    largest = nums[len(nums)-1] - K
    smallest = nums[0] + K
    ans = largest - smallest

    for i in range(len(nums)):
        print(minMaximize(nums))
