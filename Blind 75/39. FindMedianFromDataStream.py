"""
https://leetcode.com/problems/find-median-from-data-stream/

adding elements to the heap logn
removing elements to the heap logn
finding max or min in a heap O(1)

Tc: log(n)
Sc: O(n)
"""

import heapq


class MedianFinder:

    def __init__(self):  # we create two heaps small and large
        self.small = []  # max- heap #in python we initiate heaps as lists []
        self.large = []  # min- heap

    def addNum(self, num: int) -> None:
        # add all the numbers to small initially
        heapq.heappush(self.small, -1 * num)  # as max- heap multiply by -1
        
        # essentially small will contain all numbers lesser than large
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # at any point both the arrays lengths should not be differ by 2- for median
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if length is odd, so median is mid.
        if len(self.small) > len(self.large):
            return (self.small[0] * -1)
        if len(self.large) > len(self.small):
            return self.large[0]
            
            # if length is even, then median is average
        return ((self.small[0] * -1) + self.large[0]) / 2


obj = MedianFinder()
num = 5
obj.addNum(num)
num = 6
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
