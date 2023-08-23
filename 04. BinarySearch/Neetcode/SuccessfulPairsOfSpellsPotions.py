"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

Approach: sort the potions and do binary search

tc - nlogn
sc - n

"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            l = 0
            r = len(potions) - 1
            ans = 0
            while l <= r:
                m = (l+r)//2
                prod = spell * potions[m]
                if prod >= success:
                    ans = len(potions) - m
                    r = m - 1
                else:
                    l = m + 1
            res.append(ans)
        return res