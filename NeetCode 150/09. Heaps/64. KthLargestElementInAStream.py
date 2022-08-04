"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/

APPROACH: 

This is a bit tricky problem because of implementing classes. Learn python classes, objects, constructors. 
As this is finding kth largest element we need to implement heaps. 
We keep adding elements so we need to make sure our min-heap will only contain k elements 
that way kth largest element in the orginal array will be the minimum element after removing elements
then we can pop the head. 
Eg: original array [1,2,3,4,5] we need to find 3rd largest element. 
so we remove 2 elements new array [3,4,5] then we can return the head. 

Tc: 
SC: O(n)

"""
import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

    def add(self, val) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(9))
