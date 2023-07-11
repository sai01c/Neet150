"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

similar to 02. TwoPointers/Neetcode/17. LongestSubstringWithReplacementCharacters.py
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        res = 0
        for r in range(len(answerKey)):
            length = r - l + 1
            count[answerKey[r]] += 1
            
            if length - max(count.values()) > k:
                count[answerKey[l]] -= 1
                if count[answerKey[l]] == 0:
                    del count[answerKey[l]]
                l += 1
            
            res = max(res, r-l+1)
        
        return res