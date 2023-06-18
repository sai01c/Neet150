"""
https://leetcode.com/problems/best-team-with-no-conflicts/

this is similar to longest increasing subsequence
"""

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for i in range(len(scores)):
            pairs.append((ages[i], scores[i]))
        pairs.sort()
        dp = []
        for i in range(len(pairs)):
            dp.append(pairs[i][1])
        
        for i in range(len(pairs)):
            a1, s1 = pairs[i]
            for j in range(i+1, len(pairs)):
                a2, s2 = pairs[j]
                if dp[j] >= dp[i]:
                    dp[j] = max(dp[j], dp[i] + s2)
                        
        return max(dp)