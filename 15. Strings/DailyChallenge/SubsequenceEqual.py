"""
https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

"""

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            char = str1[i]
            rank1 = ord(char) - ord('a')
            rank2 = ord(str2[j]) - ord('a')
            if rank1 == 25:
                rank1 = -1
            if char == str2[j]:
                j += 1
            elif (rank1 + 1 == rank2):
                j += 1
            if j == len(str2):
                return True
        return j == len(str2)