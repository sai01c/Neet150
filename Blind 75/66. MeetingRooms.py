"""
https://www.lintcode.com/problem/920/

Approach- First, sort the intervals based on start times. 
Now check if the i1.start<i0.end

TC: O(nlogn) as we are sorting
SC:O(1)

"""

def meeting(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


print(meeting([(0, 30), (5, 10), (15, 20)]))
print(meeting([(5, 8), (9, 15)]))
