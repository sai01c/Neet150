"""
https://leetcode.com/problems/sort-an-array/

approach: use heap sort- first push and then pop
Tc: O(nlogn)
"""

import heapq


def sort(nums):
    heap = []
    res = []
    for num in nums:
        heapq.heappush(heap, num)
    while heap:
        val = heapq.heappop(heap)
        res.append(val)
    return res

print(sort([5,1,1,2,0,0]))

"""
TODO- Merge Sort

"""

