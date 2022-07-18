"""
https://leetcode.com/problems/sliding-window-maximum/

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 """


# this is a brute force solution. Using the basic sliding window concept and finding the maximum element using in-built max function.
# TC: O(n^2)
# Sc: O(n) using array
# Accepted test cases - 35 / 51 test cases passed.
import collections


def slidingWindowMaximum(nums, k):
    left = 0
    ans = 0
    res = []
    for right in range(k, len(nums) + 1):
        window = nums[left: right]
        if len(window) >= k:
            left += 1
        for num in window:
            ans = max(ans, num)
        res.append(ans)
    return res


print(slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

"""
Optimal solution O(n) 

Approach - we are going to have a queue with the indexes of the elements of nums. 
while adding we only add elements that are less, if there's an higher element then we remove the elements in the queue. Idea is to have the highest element in the queue. 
and queue should be decreasing queue. 

Now we implement sliding window concept and for every window increase the left and add the highest element from the queue (index 0) 

Tc: O(n) not sure why it is n as we have for and while. 
deque inserting deleting the element is O(1)
"""


def slidingWindowMaximum2(nums, k):
    left = 0
    indQ = collections.deque()
    res = []
    for right in range(len(nums)):
        while indQ and nums[right] > nums[indQ[-1]]:
            indQ.pop()  # remove the last element as we are comparing that to the incoming element
        indQ.append(right)

        if left > indQ[0]:  # i did not completely understand this
            # to remove the left value from the queue
            # this is like an out of bounce case- if left is increase but the elements are still in the queue.
            indQ.popleft()
            """ the above if condition is used in this case
            Input [1,-1] 1 Output [1,1] Expected [1,-1]
"""

        if right+1 > k:  # we will be shifting the pointer every iteration so every window
            left += 1
            res.append(nums[indQ[0]])
    return res
