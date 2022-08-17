"""
https://www.lintcode.com/problem/919/description

Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

Approach- create two lists for start times and end times. sort them. 
compare them and increase the count accordingly

"""


def confRooms(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    count = 0
    res = 0
    s = 0
    e = 0
    while s < len(start):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


print(confRooms([(0, 30), (5, 10), (15, 20)]))
print(confRooms([(2, 7)]))


def func(intervals):
    intervals.sort(key=lambda x: x[0])
    last = intervals[0][1]
    res = 1
    for s, e in intervals[1:]:
        if s < last:
            res += 1
        last = e
    return res


print(func([(0, 30), (5, 10), (15, 20)]))
print(func([(2, 7)]))
