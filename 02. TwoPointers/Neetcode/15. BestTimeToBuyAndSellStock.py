"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Sliding Window: initiate two pointer's left and right. if price of right is less than left, 
that means we found minP. assign left pointer to this index
calculate profit. use another variable to get max of all profits. 

TC: O(n)
SC: O(1)
"""

def maxProfit(self, prices: List[int]) -> int:
    left = 0
    right = 0
    ans = 0
    for right in range(len(prices)):
        if prices[right] < prices[left]:
            left = right
        profit = prices[right] - prices[left]
        ans = max(ans, profit)
        
    return ans

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Approach: use sliding window concept here as well,
only change is their in the first question, you need to find max profit. 
But, here you need to find all profits. 
so, after you calculate the first profit, there still may be another profit chance
so, initiate left pointer at the right index.

Tc: O(n)
Sc: O(1)

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            ans += profit
            
            if profit > 0:
                left = right
        return ans