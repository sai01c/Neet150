"""
https://leetcode.com/problems/sum-of-subarray-minimums/

Approach - we need to find smaller element
formula is (number of elements to the left of x that are smaller than x) + 1
multiplied by
(number of elements to the right of x that are smaller than x) + 1
l+1 * r+1 

tc - n
sc - n

"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            mini = float('inf')
            for j in range(i, len(arr)):
                mini = min(mini, arr[j])
                res += mini
        mod = 10 ** 9 + 7
        return res % mod
    

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        mod = 10 ** 9 + 7
        
        arr = [float('-inf')] + arr + [float('-inf')]
        
        for i in range(len(arr)):
            val = arr[i]
            while stack and val < arr[stack[-1]]:
                m = stack.pop()
                l = stack[-1]
                r = i
                res += arr[m] * (r-m) * (m-l)
            stack.append(i)
        
        return res % mod