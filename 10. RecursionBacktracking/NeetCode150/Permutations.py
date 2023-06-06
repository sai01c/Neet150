"""
https://leetcode.com/problems/permutations/

Approach - we need to create permutations of the array [1,2,3]. 
For every position we will have 3 choices initially
then next element we will have 2 and then last element we only have 1 choice.

tc - n!
sc - n + n!

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        visit = set()

        #this is backtracking template for this sort of problems. 

        def backtrack(i):
            if len(permutation) == len(nums): #base case - if it meeds our needs add the copy and return
                res.append(permutation.copy())
                return
            
            for i in range(len(nums)): #iterate through all of the elements.
                if i not in visit: 
                    #check for condition satisfying our case.
                    #using set because we need unique elements
                    permutation.append(nums[i]) #add element 
                    visit.add(i)

                    backtrack(i+1) #do recursive call on next iteration

                    permutation.pop() #after recursive call remove the element
                    visit.remove(i)

        backtrack(0)
        return res