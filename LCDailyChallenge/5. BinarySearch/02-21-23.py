"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

Approach: this is sorted array so binary search
Now, we will check if mid != mid-1 and mid != mid+1 then it is the answer
notice, the length of the array will be odd becuse there's one element with 1 count
this is the biggest logic of this question
Now, if you find mid and if mid is equal to one of its neighbours, we can divide the array into 
one odd length and one even length. Repeat until you get the mid with 1 count

Tc: O(logn)
Sc:O(1)
"""

def binary(nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + ((r-l) // 2)
        if (
            (mid - 1 < 0 or nums[mid] != nums[mid+1]) 
            and 
            (mid + 1 == len(nums) or nums[mid] != nums[mid-1]) 
            ): 
            #these conditions are edge cases if mid = 0 or mid == len(nums) - 1
            return nums[mid]
        leftSize = mid - 1 if nums[mid] == nums[mid-1] else mid
        # [1,1,2,2,3,4,4] nums[mid] = nums[mid-1] = 2. mid = 3
        #leftSize = mid - 1 = 2 even
        #[1,1,2,3,3,4,4] nums[mid] = nums[mid+1] = 3. mid = 3
        #leftSize = mid = 3
        if leftSize % 2 == 0:
            left = mid + 1
        else:
            right = mid - 1