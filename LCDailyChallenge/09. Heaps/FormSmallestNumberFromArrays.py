"""
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

Approach - use heaps to get the minimum element

tc - O(n logn)
sc- O(n)
"""

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set2 = set(nums2)
        heap = []
        for n in nums1: #first check for any common elements
            if n in set2:
                heapq.heappush(heap, n)
                
        if heap: return heapq.heappop(heap) #return min of the common elements
        
        heapq.heapify(nums1)
        heapq.heapify(nums2)
        
        #if no common elements - get the minimum of the both nums
        min1 = heapq.heappop(nums1) 
        min2 = heapq.heappop(nums2)
        
        #based on the min get the sum
        if min1 > min2:
            return min2*10 + min1
        else:
            return min1*10 + min2
        
        
