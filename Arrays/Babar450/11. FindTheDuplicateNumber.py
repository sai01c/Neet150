"""
this is """


def duplicate(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for i, j in count.items():
        if j != 1:
            return i


nums = [1, 3, 4, 2, 2]
print(duplicate(nums))
