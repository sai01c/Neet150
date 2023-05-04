import heapq
import random

("https://leetcode.com/problems/kth-largest-element-in-an-array/")


"""
Create three array's based on the randomly choosen pivot.
Repeat the same process with the array's.
Quick Select-
worst case O(n^2)
average case O(n)
"""


def kthmin(arr, k):
    rando = random.choice(arr)
    left = [x for x in arr if x < rando]
    right = [x for x in arr if x > rando]
    mid = [x for x in arr if x == rando]

    l = len(left)
    m = len(mid)

    if (k <= l):
        return kthmin(left, k)
    elif (k > (l+m)):
        return kthmin(right, k - (l + m))
    else:
        return mid[0]


nums = [7, 10, 4, 3, 20, 15]
k = 3
print(kthmin(nums, k))


"""
Heapify will convert the array to min-heap.
Now use heappop to remove the last element.
Time complexity doubt-
"""


def kthminheap(nums, k):
    heapq.heapify(nums)
    iter = 1
    while iter <= k:
        res = heapq.heappop(nums)
        iter += 1
    return res


nums = [7, 10, 4, 3, 20, 15]
k = 2
print(kthminheap(nums, k))

"""
same method as min-heap but we need to change the iteration direction to get the max element.
TC: doubt
"""


def kthmaxheap(nums, k):
    heapq.heapify(nums)
    iter = len(nums)
    while iter >= k:
        res = heapq.heappop(nums)
        iter -= 1
    return res


nums = [7, 10, 4, 3, 20, 15]
k = 2
print(kthmaxheap(nums, k))


"""
same as quick select but sorting the array in descending order
"""


def kthmax(arr, k):
    rando = random.choice(arr)
    left = [x for x in arr if x > rando]
    right = [x for x in arr if x < rando]
    mid = [x for x in arr if x == rando]

    l = len(left)
    m = len(mid)

    if (k <= l):
        return kthmax(left, k)
    elif (k > (l+m)):
        return kthmax(right, k - (l + m))
    else:
        return mid[0]


nums = [7, 10, 4, 3, 20, 15]
k = 2
print(kthmax(nums, k))
