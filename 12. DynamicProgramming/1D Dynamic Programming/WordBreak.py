"""
https://leetcode.com/problems/word-break/

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                l = len(w)
                if (i + l) <= len(s) and s[i:i+l] == w:
                    dp[i] = dp[i+l]
                if dp[i]:
                    break
        
        return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @lru_cache(maxsize = 128)
        def backtrack(i):
            if i >= len(s):
                return True
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string in wordDict:
                    if backtrack(j+1):
                        return True
            
            return False
        
        return backtrack(0)
