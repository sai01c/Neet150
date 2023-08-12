"""
https://leetcode.com/problems/brick-wall/
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = {0: 0}
        for w in wall:
            pre = 0
            for num in w[:-1]:
                pre += num
                if pre in count:
                    count[pre] += 1
                else:
                    count[pre] = 1
        N = len(wall)
        res = float('inf')
        for k, v in count.items():
            res = min(res, N - v)
        return res