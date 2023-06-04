"""
https://leetcode.com/problems/restore-ip-addresses/

"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        curr = ""
        if len(s) >= 13: return res
        def backtrack(i, curr, dots):
            if i>=len(s) and dots==4:
                res.append(curr[:-1])
                return
            if dots>4:
                return
            for j in range(i, min(i+3, len(s))):
                if (int(s[i:j+1]) < 256 and (i==j or s[i] != "0")): #this is avoid leading zeroes
                    backtrack(j+1, curr+s[i:j+1]+".", dots+1)
        backtrack(0, "", 0)
        return res
                    