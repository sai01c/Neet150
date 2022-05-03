"""
iterate through the array and if you find any negative number, swap 
"""


def negative(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            swap(nums, i, j)
            j += 1
    return nums


def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp


arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(negative(arr1))
