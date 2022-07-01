"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Approach 1 EXPLANATION: iterate throught the prices and first find out the minimum price. 
calculate profit and find out the maximum profit.

TC: O(n)
SC: O(1)
"""


def stock1(prices):
    minPrice = float("inf")
    maxProfit = 0
    for price in prices:
        minPrice = min(price, minPrice)
        profit = price - minPrice
        maxProfit = max(profit, maxProfit)
    return maxProfit


print(stock1([7, 1, 5, 3, 6, 4]))
print(stock1([7, 6, 4, 3, 1]))

"""
Approach 2: use sliding window pattern - left will be fixed. right will iterate through the array. 
update the left pointer based on condition 
subtract right - left to give the profit. 
use max to get the highest profit. 

Tc: O(n)
Sc: O(1)

"""


def stock2(prices):
    left = 0
    res = 0
    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right
        res = max(res, prices[right] - prices[left])
    return res


print(stock2([7, 1, 5, 3, 6, 4]))
print(stock2([7, 6, 4, 3, 1]))
