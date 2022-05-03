nums = [1000, 11, 445, 1, 330, 3000]

"""
First, compare first two elements and assign the max and min among those two. 
Now, compare the max and min with the rest of the elements and update the max and min.
Linear Search method

TC O(n)
not the optimal method
"""


def maxandmin(nums):
    if nums[0] < nums[1]:
        mini = nums[0]
        maxi = nums[1]
    else:
        mini = nums[1]
        maxi = nums[0]

    for i in range(2, len(nums)):
        if nums[i] > maxi:
            maxi = nums[i]
        if nums[i] < mini:
            mini = nums[i]
    return mini, maxi


print(maxandmin(nums))
