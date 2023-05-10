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
            prevEnd = min(end, prevEnd) #why min?
            #if end is min, we can include more intervals. 
            # if more intervals are included then less intervals to exclude which we want
        else:
            prevEnd = end
    return res


print(NonOverlap([[1, 2], [1, 2], [1, 2]]))