"""
https://leetcode.com/problems/container-with-most-water/

Explanation: we need to find the max area of rectangle. 
use area formula - length * breadth
length will be the min of left or right as water will overflow. 
breadth will be the difference between left and right. 
breadth is already maximum as left is 0 and right is len-1
max will be the difference between left and right. 
and we increase the left and right pointers to try for different lengths and breadths. 
"""


def maxArea(height):

    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:  # compute the value after the while loop
        area = (right-left)*min(height[left], height[right])
        if height[left] < height[right]:  # doubt on why we doing this exactly - we want to consider best possible length
            left += 1
        else:
            right -= 1
        ans = max(ans, area)
    return ans
