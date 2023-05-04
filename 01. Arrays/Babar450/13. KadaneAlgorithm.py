"""
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
"""

runSum = 0
nums = [1, 2, 3, -2, 5]
maxi = nums[0]
for _ in nums:
    if runSum < 0:
        runSum = 0
    runSum += _
    maxi = max(runSum, maxi)
print(maxi)
