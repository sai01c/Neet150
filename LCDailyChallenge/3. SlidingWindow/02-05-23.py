"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Solution: First, anagram means count of variables will be same. we can use dict to measure this. 
second, we use sliding window concept to move through the string. at O(N) instead of having two pointers.
Now, as we move through sliding window, we add right count to dic. 
we check our current substring count and p count if they are same
we need to address two other issues, if len of substring increases more than p, 
then we remove the left count from dict and we increase the left.
we also delete any elements in dict with count 0. 

TC: O(p + s)
Sc: O(s + p)

Solved this problem without any help, felt good. 
"""

from ast import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = {}
        for i in p:
            pc[i] = pc.get(i, 0) + 1
        print("pc", pc)   
        res = []
        sc = {}
        left = 0
        for right in range(len(s)):
            sub = s[left: right + 1]
            sc[s[right]] = sc.get(s[right], 0) + 1
            print("sc", sc)
            if sc == pc:
                res.append(left)
            if len(sub) >= len(p):
                sc[s[left]] -= 1
                if sc[s[left]] == 0: del sc[s[left]]
                left += 1
        
        return res

