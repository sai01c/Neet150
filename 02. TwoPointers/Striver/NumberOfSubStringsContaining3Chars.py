"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Approach - substring so sliding window
key here is if our length of dic is 3 that means all the subarrays from this right
will satisfy our condition
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        dic = defaultdict(int)
        res = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            
            while len(dic) == 3:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
                
                temp = (len(s) - r)
                res += temp
                
                
        return res
        