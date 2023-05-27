"""
https://leetcode.com/problems/hand-of-straights/

Approach - 

tc
sc
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        nums = list(count.keys())
        heapq.heapify(nums)
        
        while nums:
            start = nums[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != nums[0]:
                        return False
                    heapq.heappop(nums)
        
        return True
            
            