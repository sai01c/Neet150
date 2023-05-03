"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Approach - here trick is we will maintain a subarray of length total - k and we 
don't include the sum of these numbers in our output. we keep moving this subarray to right
and changing sum to find the max sum

this is most asked Google question of 2021

tc - n
sc - n
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        #length of our subarray
        r = len(cardPoints) - k 
        #find the initial sum
        total = sum(cardPoints[r:])
        res = total
        
        while r < len(cardPoints):
            #basically, moving subarray to right
            total += cardPoints[l] #add left number
            total -= cardPoints[r] #subtract right number
            res = max(res, total)
            l += 1
            r += 1
        
        return res