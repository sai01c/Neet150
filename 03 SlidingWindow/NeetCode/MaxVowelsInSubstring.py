"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        visit = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        count = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in visit:
                count += 1

            length = r - l + 1
            if length > k:
                if s[l] in visit:
                    count -= 1
                l += 1
            ans = max(ans, count)

        
        return ans
        