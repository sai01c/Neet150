class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        self.reverse(nums, n-k ,n - 1)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, 0, n-1)
        
    def reverse(self, nums, l, r):
        
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
            
        return nums
        