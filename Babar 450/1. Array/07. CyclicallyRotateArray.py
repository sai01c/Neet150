"""
rotating the array- reversing the array three time. 
First, reverse the entire array. 
Second, reverse the first k elements. 
Third, reverse the next [k+1] elements. 
"""
("https://leetcode.com/problems/rotate-array/")


def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


def swap(l, r):
    temp = l
    l = r
    r = temp


def rotate(nums, k):
    k = k % len(nums)  # not understood. this is if len(nums) < k
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    return nums


input = [1, 2, 3, 4, 5]
x = 2
output = [4, 5, 1, 2, 3]
print(rotate(input, x))

# rotate by 1
input2 = [9, 8, 7, 6, 4, 2, 1, 3]
output = [3, 9, 8, 7, 6, 4, 2, 1]

"""
First, assign the last element to a variable. 
Now, iterate reverse direction and shift the elements by 1 index. 
"""


def rotateOne(arr):
    lastDigit = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = lastDigit
    return arr


print(rotateOne(input2))
