"""
https://leetcode.com/problems/maximum-number-of-removable-characters/
"""

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(s1, s2):
            if len(s2) > len(s1):
                return False
            q = collections.deque(s2)
            for i in range(len(s1)):
                if q and s1[i] == q[0]:
                    q.popleft()
            if not q:
                return True
            return False
        
        def helper(m):
            visit = set(removable[:m])
            res = ""
            for i in range(len(s)):
                if i in visit:
                    continue
                res += s[i]
            if isSubsequence(res, p):
                return True
            else:
                return False
            
        l = 0
        r = len(removable)
        ans = 0
        while l <= r:
            m = (l+r) // 2
            if helper(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans