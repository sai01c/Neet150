"""
https://leetcode.com/problems/find-right-interval/
"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        end = []
        res = [-1] * len(intervals)
        
        for i in range(len(intervals)):
            s, e = intervals[i]
            start.append((s, i))
            end.append((e, i))
        start.sort()
        
        for e, i in end:
            l = 0
            r = len(start) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if start[m][0] < e:
                    l = m + 1
                else:
                    ans = start[m][1]
                    r = m - 1
            res[i] = ans
        return res
