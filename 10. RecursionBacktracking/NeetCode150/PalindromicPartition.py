"""
https://leetcode.com/problems/palindrome-partitioning/

Approach: this is another backtracking template problem
First we check for partition if it satisfies the palindrom, we will do backtracking on next part of string

tc - n * n**n but for tighter bound refer this
https://stackoverflow.com/questions/24591616/whats-the-time-complexity-of-this-algorithm-for-palindrome-partitioning
sc - n

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        #regular backtracking template
        def backtrack(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.palidrome(s, i, j):
                    
                    partition.append(s[i:j+1])
                    backtrack(j+1)

                    partition.pop()

        backtrack(0)
        return res
    
    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True