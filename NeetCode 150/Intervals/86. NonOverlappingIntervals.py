"""
https://leetcode.com/problems/non-overlapping-intervals/

Approach: this is similar to merge intervals, first you sort the intervals based on start. 
check if the new interval is less than previous end. 
then update the prev end based on the condtions

TC: O(nlogn) as we are sorting here
SC: O(1) creating res variable
"""


def NonOverlap(intervals):
    intervals.sort(key=lambda x: x[0])
    prevEnd = intervals[0][1]
    res = 0
    for start, end in intervals[1:]:
        if start < prevEnd:
            res += 1
            # here we want to remove minimum intervals. so
            prevEnd = min(end, prevEnd)
            # if we have min end that means max intervals can be there and min intervals can be removed
        else:  # we just update the end for non overlapping ones
            prevEnd = end
    return res


print(NonOverlap([[1, 2], [1, 2], [1, 2]]))
