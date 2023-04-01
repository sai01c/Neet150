"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

This is a bit tricky problem because of implementing classes. Learn python classes, objects, constructors. 
As this is finding kth largest element we need to implement heaps. 
We keep adding elements so we need to make sure our min-heap will only contain k elements 
that way kth largest element in the orginal array will be the minimum element after removing elements
then we can pop the head. 
Eg: original array [1,2,3,4,5] we need to find 3rd largest element. 
so we remove 2 elements new array [3,4,5] then we can return the head. 
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
