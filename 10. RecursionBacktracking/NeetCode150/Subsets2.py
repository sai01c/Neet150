"""
https://leetcode.com/problems/subsets-ii/

Approach - this is backtracking problem. similar to subsets 1
But, here array is not unique. And, we need to find unique subsets.
To avoid duplicate elements first we sort the array and then we check 
for i+1 == i if yes then shift the pointer

tc - n * 2**n
sc- n * 2**n

"""

def subsetsWithDup(nums):
    res = []
    subset = []
    nums.sort() #sort the numbers so that same numbers can be side by side

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        #first case - including element
        subset.append(nums[i])
        backtrack(i+1)

        #second case - not include element
        subset.pop()
        while (i + 1 < len(nums) and nums[i] == nums[i+1]): #shift the pointer if elements are same
            i += 1 #notice using while loop we shift until we find diff elements.
        backtrack(i+1)

    backtrack(0)
    return res