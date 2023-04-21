"""
https://leetcode.com/problems/isomorphic-strings/

approach

tc
sc
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)
        
        for i in range(len(s)):
            dic1[s[i]].append(i)
            dic2[t[i]].append(i)
        
        arr1, arr2 = [], []
        
        for val in dic1.values():
            arr1.append(val)
        
        for val in dic2.values():
            arr2.append(val)
        
        return arr1 == arr2