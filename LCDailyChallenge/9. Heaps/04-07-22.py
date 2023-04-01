"""
https://leetcode.com/problems/last-stone-weight/

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

As it is a maximum problem, idea is to use heap. 
using heap we can get the first largest and second largest elements. 
if the first and second are different, push the difference to the heap
continue this process as long as the heap has more than 1 element
"""

import heapq


def lastStone(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if first != second:
            heapq.heappush(stones, first - second)
    # this is because if input is [2,2] both the elements will be popped and stones will be [] so append 0 to stones.
    stones.append(0)
    # appending won't affect our answer because we only need 0th index in other cases.
    return abs(stones[0])


input = [2, 7, 4, 1, 8, 1]
print(lastStone(input))
