"""

Selection sort: first select the min value from the elements 
and now swap the minimum element and first element.
In-place sorting algorithm

"""

nums = [2, 7, 4, 3, 9]


def selectionSort(nums):
    for i in range(len(nums)):
        minvalue = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minvalue]:
                minvalue = j
        temp = nums[i]
        nums[i] = nums[minvalue]
        nums[minvalue] = temp

    return nums


print(selectionSort(nums))
