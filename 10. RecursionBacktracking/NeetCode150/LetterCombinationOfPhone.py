"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Approach - this is another backtracking template because we have to make decision at each level.
 
tc - 4 ** len(digits). 4 because for digits 7 and 9 we will have 4 char's.
sc - n * 4**n
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []

        #regular backtracking template
        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr) #why not copy here
                return
            
            for char in digitToChar[digits[i]]:
                backtrack(i+1, curr+char) #instead of doing append and pop we are directly adding 
                #char to curr in the function arguement because removing from string can be tricky
                
        if digits:
            backtrack(0, "")
        return res
                
                