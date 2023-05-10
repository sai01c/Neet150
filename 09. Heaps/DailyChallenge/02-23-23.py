"""
https://leetcode.com/problems/ipo/submissions/

Brute Force approach: I did the same as optimal except I did not use heap for capital.

TLE 33/35 cases.

"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        have = w 
        ans = w
        while k > 0:
            profit = 0
            heap = []
            for i in range(len(capital)):
                need = capital[i]
                if have >= need:
                    heapq.heappush(heap, (- 1 * profits[i], i)) 
            if heap: 
                profit, i = heapq.heappop(heap) 
            else:
                return ans
            profits.pop(i)
            capital.pop(i)
            profit = -1 * profit
            ans += (profit)
            have += profit
            k -= 1
        return ans
    
"""
Optimal Approach: have two heaps - one min heap for capital other max heap for profits
while iterating over the min heap check if our current profit is more than minHeap values. 
Add all those values which satisfy this condition. Now, out of all the profits available select 
maximum profit. 

Tc: k log(n)
Sc: O(n)

"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapacity = []
        for c, p in zip(capital, profits):
            minCapacity.append((c, p))
        heapq.heapify(minCapacity)
        
        for i in range(k):
            while minCapacity and w >= minCapacity[0][0]:
                c, p = heapq.heappop(minCapacity)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            
            w += -1 * heapq.heappop(maxProfit)
        return w