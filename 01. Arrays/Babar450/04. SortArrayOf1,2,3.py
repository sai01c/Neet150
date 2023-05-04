"""
Time complexity is O(3n)
Space complexity is O(n)
"""


def sort(nums):
    ones = [x for x in nums if x == 1]
    twos = [x for x in nums if x == 2]
    zeros = [x for x in nums if x == 0]

    return (zeros + ones + twos)


arr = [0, 0, 1, 2, 2]
print(sort(arr))

"""
Time complexity is O(n)
Space Complexit is O(1)
"""


def dutchnational(nums):
    start = 0
    end = len(nums) - 1
    mid = end//2

    while mid <= end:
        if nums[mid] < 1:
            swap(nums, start, mid)
            #mid += 1
            start += 1
        elif nums[mid] > 1:
            swap(nums, mid, end)
            end -= 1
        else:
            mid += 1
    return nums


def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp


print(dutchnational(arr))


"""
[2, 1, 0, 1, 2]
| start | mid | end |
0 0 4 
0 0 3 [2,1,0,1,2]
0 0 2 [1 ,1 ,0, 2, 2]
0 1 2
0 2 2
"""

arr1 = [0, 1, 0]
print(dutchnational(arr1))
