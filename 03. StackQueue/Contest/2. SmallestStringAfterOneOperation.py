"""
https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

very edgy tricky cases.
we are using queue because we need to take the left variables to a and right variables to a

"""

class Solution:
    def smallestString(self, s: str) -> str:
        q = collections.deque(list(s))
        res = ""
        while q and q[0] == 'a':
            res += q[0]
            q.popleft()
        done = False
        while q and q[0] != 'a':
            done = True
            c = q[0]
            res += chr(ord(c) - 1)
            q.popleft()
            
        while q:
            res += q[0]
            q.popleft()
        
        if done:
            return res
        else:
            return s[:-1] + 'z'