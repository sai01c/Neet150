"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

"""

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = []
        for i in range(10):
            nums.append(i)
            
        def backtrack(i, curr):
            if len(curr) == n:
                res.append(int(curr))
                return
            if len(curr) > n:
                return
            for num in nums:
                if curr and curr[0] == "0":
                    continue
                if (
                    len(curr)==0 or 
                (len(curr) >= 1 and abs(int(curr[-1])-num) == k)
                ):
                    backtrack(i+1, curr+str(num))
        res = []
        backtrack(0, "")
        return res