"""
https://leetcode.com/problems/top-k-frequent-elements/

Approach: first, use a count dictionary i.e element:frequenctcount
now, sort them in decreasing order of count
now iterate through the sort list and append the key i.e element

Tc: O(n logn) sorting the dictionary based on counts. 
Sc: O(n) using dictionary and res array
"""

import heapq


def topKfrequent(nums, k):
    count = {}
    res = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sortCount = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sortCount)
    for i in range(k):
        res.append(sortCount[i][0])
    return res


print(topKfrequent([1, 1, 1, 10,  2, 2, 3], 2))

"""
Approach: create the count dictionary based on the frequency
create a heap and add (value, frequency) to the heap
return the k max frequencies
multiply by -1 as we want maximum

Tc: O(n logn) as we are using heap. to push elements to heap O(nlogn)
Sc: O(n) using dict and heap
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        heap = []
        for num, cou in count.items():
            heapq.heappush(heap, (-1 * cou, num))
        res = []
        for i in range(k):
            cou, num = heapq.heappop(heap)
            res.append(num)

        return res
