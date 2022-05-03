"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

EXPLANATION: iterate throught the prices and first find out the minimum price. 
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
