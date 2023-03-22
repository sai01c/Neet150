"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach: 
if heights of rectangles are continously increasing it is easy to calculate height = h * len(h) - index
but if heights may be decreasing or increasing
if height is decreasing we can stop including that height and calculate the area for that. 
So, consider a stack and if the height is decreasing remove that height and calculate area

Tc: O(n) for loop accoring to neetcode. But, we used a while loop inside for loop so it should be n^2. 
Sc: O(n) for stack space. 
"""


def rectangeHist(heights):
    stack = []
    maxArea = 0
    for index, height in enumerate(heights):
        start = index
        
        while stack and height < stack[-1][1]:
            # remove the decrease height
            stackindex, stackheight = stack.pop()  
            # calculate the area until the removed height.
            maxArea = max(maxArea, stackheight * (index - stackindex))
            # we want to continue including the width.
            start = stackindex  
            
        stack.append((start, height))

    #here, we are iterating over stack because if we have all increasing heights
    for index, height in stack:  # this is if all the heights are increasing
        maxArea = max(maxArea, height * (len(heights) - index))

    return maxArea


print(rectangeHist([2, 1, 5, 6, 2, 3]))
