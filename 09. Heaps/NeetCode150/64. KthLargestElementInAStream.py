"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

APPROACH: 

This is a bit tricky problem because of implementing classes. Learn python classes, objects, constructors. 
As this is finding kth largest element we need to implement heaps. 
We keep adding elements so we need to make sure our min-heap will only contain k elements 
that way kth largest element in the orginal array will be the minimum element after removing elements
then we can pop the head. 

This approach will work because our k value is fixed. 

Eg: original array [1,2,3,4,5] we need to find 3rd largest element. 
so we remove 2 elements new array [3,4,5] then we can return the 0th index element. 

Tc: O(logn) for adding and removing elements from the heap. 
SC: O(n) as we are using heap

"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for val in nums:
            heapq.heappush(self.heap, val)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) #adding single element is logn.
        #we always add new value but we restrict the size to k. if size exceeds more than k, we pop elements.
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0] #return 0th element because it is the min element or kth greater element.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)