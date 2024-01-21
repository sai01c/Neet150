

# Bubble Sort

"""
Idea is to move the largest element to end of the array for each iteration.
We compare the arr[1] and arr[2] and swap them. Now we compare arr[2], arr[3] and swap them. 
Next, we compare arr[3], arr[4] and swap them. 
Eg. [2,1,4,0] we check 3 times namely (2,1), (1,4), (4,0)
Now, we repeat the same process for n-1 times.

In-place algorithm.
TC: O(n^n)

"""
nums = [8, 9, 3, 2, 4, 5, 6, 7, 3]
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
