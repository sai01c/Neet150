"""
https://leetcode.com/problems/smallest-number-in-infinite-set/

Approach - first, add all the positive numbers to the heap.
use heap to remove the smallest number
use dic to check if element is in the heap or not

tc - nlogn
sc - n

"""

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.dic = defaultdict(int)
        
        for num in range(1, 1001):
            heapq.heappush(self.heap, num)
            self.dic[num] += 1

    def popSmallest(self) -> int:
        val = heapq.heappop(self.heap)
        self.dic[val] = 0
        del self.dic[val]
        
        return val

    def addBack(self, num: int) -> None:
        if num not in self.dic:
            heapq.heappush(self.heap, num)
            self.dic[num] += 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)