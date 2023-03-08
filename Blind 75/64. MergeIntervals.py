"""

https://leetcode.com/problems/merge-intervals/

Approach: First we need to sort them based on the intervals[i][0]. 
Now, add the first interval and iterate through the rest of them and check if the start is less than end of the last interval
then try to find the max of those two intervals. 
else, append the interval to the result. 

TC O(nlogn) as we are sorting here
SC: O(n) we are using a res array.

"""

def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    res.append(intervals[0])
    for i in range(1, len(intervals)):
        lastEnd = res[-1][1]
        if intervals[i][0] <= lastEnd:
            res[-1][1] = max(lastEnd, intervals[i][1])
        else:
            res.append(intervals[i])
    return res

print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
