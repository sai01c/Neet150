"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

tc - n**n
sc - n

"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def backtrack(i, curr):
            if i >= len(arr):
                res.append(len(curr))
                return
            #this line is very imp - imagine a case where we might not reach the end of
            #the array but there will be a unique string at index less than len(arr)
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
        