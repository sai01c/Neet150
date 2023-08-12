"""
https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

typical sliding window problem
"""

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        temp = 0
        for r in range(len(s)):
            if r > 0 and s[r] == s[r-1]:
                temp += 1
            while temp > 1 and l < r-1:
                if s[l] == s[l+1]:
                    temp -= 1
                l += 1
            length = r - l + 1
            ans = max(ans, length)
        return ans