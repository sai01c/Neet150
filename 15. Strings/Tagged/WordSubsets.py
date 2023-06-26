"""
https://leetcode.com/problems/word-subsets/

"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count1 = [0] * 26
        count2 = [0] * 26
        
        for word in words2:
            count = Counter(word)
            for char, fre in count.items():
                val = ord(char) - ord('a')
                count2[val] = max(count2[val], fre) #this is the trick here
        
        def helper(arr1, arr2):
            for i in range(len(arr2)):
                if arr2[i] > 0:
                    if arr1[i] < arr2[i]:
                        return False
            return True
        
        res = []
        for word in words1:
            count1 = [0] * 26
            for char in word:
                val = ord(char) - ord('a')
                count1[val] += 1
            if helper(count1, count2):
                res.append(word)          
        
        return res
                
            