"""
https://leetcode.com/problems/online-stock-span/

Approach - read given example to understand
we want number of days stock prices are less or equal to current price
eg [7,34,1,2] current is 8 for days 1,2,8 stock price is less or equal to 8

tc - 1 because while loop does not depend on input size
sc - n
"""

class StockSpanner:

    def __init__(self):
        self.i = -1
        self.stack = []
        self.stack.append((-1, float('inf')))

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
        
        val = self.stack[-1][0]
        self.stack.append((self.i, price))
        return self.i - val
