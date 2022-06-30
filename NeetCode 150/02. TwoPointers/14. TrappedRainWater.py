"""
https://leetcode.com/problems/trapping-rain-water/submissions/

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Approach: this is a 2D graph looking like question. 
Idea is to use two pointer and shift the pointers. 
Initially, have the maximum height at default pointers location. 
after shifting the pointer, we will computer the new maximum height
subtract the maximum height - current height

TC: O(n) while loop
SC: O(1) only pointers
"""


def trap(height):
    left = 0
    right = len(height) - 1

    maxHeightLeft = height[left]
    maxHeightRight = height[right]

    res = 0

    while left < right:  # as usual two pointer and shift the pointers based on which is min/max
        if height[left] < height[right]:
            left += 1
            # after shifing the pointer compare the new Maximum
            maxHeightLeft = max(maxHeightLeft, height[left])
            # we want trapped water so maximum minus current
            res += maxHeightLeft - height[left]

        else:
            right -= 1
            maxHeightRight = max(maxHeightRight, height[right])
            res += maxHeightRight - height[right]

    return res


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
