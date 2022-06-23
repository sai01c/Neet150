"""
https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Explanation: we need to find the max area of rectangle. 
use area formula - length * breadth
length will be the min of left or right as water will overflow. 
breadth will be the difference between left and right. breadth is already maximum as left is 0 and right is len-1
and, we increase the left and right pointers to get the maximum area. 
if we increase the pointers based on max length then we'll get the max area.  

Tc: O(n) one while loop
Sc: O(1) only pointers
"""


def maxArea(height):

    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:  # compute the value after the while loop
        area = (right-left)*min(height[left], height[right])
        if height[left] < height[right]:  # to get the max length then we can get max area
            left += 1  # we are eliminating min length values.
        else:
            right -= 1
        ans = max(ans, area)
    return ans
