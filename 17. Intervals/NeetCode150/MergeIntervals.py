"""
https://leetcode.com/problems/merge-intervals/

Approach: First we need to sort them based on the intervals[i][0]. 
Now, add the first interval and iterate through the rest of them and check if the start is less than end of the last interval
then try to find the max of those two intervals. 
else, append the interval to the result. 

TC O(nlogn) as we are sorting here
SC: O(n) we are using a res array.

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for s, e in intervals[1:]:
            lastEnd = res[-1][1] #update last always
            if s <= lastEnd: # if they overlap find the max and update the res with max
                res[-1][1] = max(e, lastEnd)
            else: # if they don't overlap add the interval
                res.append([start,end])
                
        return res
