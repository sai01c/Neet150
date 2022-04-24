"""

https://leetcode.com/problems/non-overlapping-intervals/

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Approach: this is similar to merge intervals, first you sort the intervals based on start. 
check if the new interval is less than previous end. 
then update the prev end based on the condtions

TC: O(n) iterating through the intervals once
SC: O(1) creating res variable
"""


def NonOverlap(intervals):
    intervals.sort(key=lambda x: x[0])
    prevEnd = intervals[0][1]
    res = 0
    for start, end in intervals[1:]:
        if start < prevEnd:
            res += 1
            prevEnd = min(end, prevEnd)
        else:
            prevEnd = end
    return res


print(NonOverlap([[1, 2], [1, 2], [1, 2]]))
