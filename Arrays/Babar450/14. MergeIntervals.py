"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i-1][1]:
