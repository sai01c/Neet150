"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach: 


Tc - 
Sc - 
"""


# this is merge sort solution - not recommended.
class Solution: 
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i = 0
        j = 0
        k = 0
        m = len(nums1)
        n = len(nums2)
        array = [0] * (m+n)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                array[k] = nums1[i]
                i += 1
                k += 1
            else:
                array[k] = nums2[j]
                j += 1
                k += 1
        while i < len(nums1):
            array[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            array[k] = nums2[j]
            j += 1
            k += 1
        n = len(array)
        if n % 2 == 0:
            return (array[n//2] + array[(n//2) - 1])/2
        else:
            return array[(n//2)]

