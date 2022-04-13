"""
https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Explanation: we need to find the max area of rectangle. 
use area formula - length * breadth
length will be the min of left or right as water will overflow. 
max will be the difference between left and right. 
and we increase the left and right pointers to try for different lengths and breadths. 
"""


def maxArea(height):

    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:
        area = (right-left)*min(height[left], height[right])
        if height[left] < height[right]:  # doubt on why we doing this exactly
            left += 1
        else:
            right -= 1
        ans = max(ans, area)
    return ans
