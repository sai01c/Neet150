"""
https://leetcode.com/problems/combination-sum-iii/

tc - 
sc - 
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        sub = []
        nums = [1,2,3,4,5,6,7,8,9]
        
        def backtrack(i, total):
            if total==n and len(sub) == k:
                res.append(sub.copy())
                return
            if i>=len(nums) or total>n:
                return
            sub.append(nums[i])
            total += nums[i]
            backtrack(i+1, total)
            sub.pop()
            total -= nums[i]
            backtrack(i+1, total)
            
        backtrack(0, 0)
        return res

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        target = n
        res = []
        sub = []
        visit = set()
        
        def backtrack(i, total):
            if total == target and len(sub) == k:
                res.append(sub.copy())
                return
            if i >= len(nums) or len(sub) > k:
                return
            for j in range(i, len(nums)):
                if j not in visit:
                    sub.append(nums[j])
                    visit.add(j)
                    backtrack(j+1, total+nums[j])
                    visit.remove(j)
                    sub.pop()
                
        backtrack(0, 0)
        return res