"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

Approach: sort the potions and do binary search

tc - nlogn
sc - n

"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() #sort the potions
        res = []
        
        for s in spells:
            ans = 0 #initiate pointers for each spell
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left+right) // 2
                if (potions[mid] * s) >= success: #satisifies our requirement
                    ans += (right-mid + 1) #if mid satisfies, all elements right to mid will satisfy.
                    right = mid - 1 #shift the pointer
                else:
                    left = mid + 1
            res.append(ans)
        return res