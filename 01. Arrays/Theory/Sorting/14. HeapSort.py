"""
APPROACH: 

- declare heap 
- push all the elements O(nlogn)
- pop all the elements and append to the res array O(nlogn)


TC: O(n logn)

"""

import heapq


nums = [3, 2, 9, 7, 8, 1]

heap = []
for num in nums:
    heapq.heappush(heap, num)  # inserting elements logn

print(heap)

res = []
# as we are doing n times, time complexity is n logn.
for i in range(len(heap)):
    res.append(heapq.heappop(heap))  # deleting elements logn

print(res)
