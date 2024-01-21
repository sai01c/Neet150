"""

Insertion Sort: 
we start from index 1 and then go backwards and compare j-1 and jth elements 
and swap them based on 

TC: O(n^2)

"""


def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            swap(nums[j-1], nums[j])
            j -= 1
    return nums


def swap(a, b):
    temp = a
    a = b
    b = temp

    return (a, b)


print(insertionSort([3, 1, 5, 8, 6, 2, 4]))
