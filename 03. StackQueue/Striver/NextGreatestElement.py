"""
https://leetcode.com/problems/next-greater-element-i/

Approach - montonic stack because we need to compare one element to other elements
we maintain a dic to store the indices of nums1
while iterating over nums2 find the greatest element
add to the stack only if it is present in dic because we only need to find the next greatest elements of these

tc - n
sc - n
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            dic[nums1[i]] = i
        stack = []
        
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                ind = dic[val]
                res[ind] = nums2[i]
            
            if nums2[i] in dic:
                stack.append(nums2[i])
        
        return res
            
                    
        
