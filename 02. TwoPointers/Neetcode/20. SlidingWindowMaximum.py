"""
https://leetcode.com/problems/sliding-window-maximum/

Optimal solution O(n) 

Approach - we are going to have a queue with the indexes of the elements of nums. 
while adding we only add elements that are less, if there's an higher element then we remove the elements in the queue. Idea is to have the highest element in the queue. 
and queue should be decreasing queue. 

Now we implement sliding window concept and for every window increase the left and add the highest element from the queue (index 0) 

Tc: O(n) inside while we are adding and removing element to queue which is O(1) so total O(n)
deque inserting deleting the element is O(1)

TODO
"""


def slidingWindowMaximum2(nums, k):
    left = 0
    indQ = collections.deque()
    res = []
    for right in range(len(nums)):
        while indQ and nums[right] > nums[indQ[-1]]: #accessing is O(1) 
            indQ.pop()  # remove the last element as we are comparing that to the incoming element
        indQ.append(right) #adding and removing element to deque is O(1) 

        if left > indQ[0]:  
            #this is when the window has shifted but queue still has the element from the previous window
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


