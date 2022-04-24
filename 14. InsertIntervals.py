"""
https://leetcode.com/problems/insert-interval/

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

First, we check if the end of new interval is less than start of the ith interval
next, if the start of the newinterval is more than end of the ith interval
else, we find the min and max of the newInterval and add it to the result array
practice this on paper to get better idea

TC: O(n) iterating through the intervals once
SC: O(n) as we are creating result array
"""


def InsertInterval(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
    res.append(newInterval)
    return res


print(InsertInterval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4.8]))
