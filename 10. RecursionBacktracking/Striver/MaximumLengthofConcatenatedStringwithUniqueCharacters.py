"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def backtrack(i, curr):
            if i >= len(arr):
                res.append(len(curr))
                return
            res.append(len(curr))
            for j in range(i, len(arr)):
                #char in arr[j] not in curr
                if self.helper(arr[j], curr):
                    backtrack(j+1, curr+arr[j])
        
        backtrack(0, "")
        return max(res)
    
    def helper(self, a, b):
        s1 = set(a)
        s2 = set(b)
        if len(a) != len(s1):
            return False
        if len(b) != len(s2):
            return False
        for char in s1:
            if char in s2:
                return False
        return True
        