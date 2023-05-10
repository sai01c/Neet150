"""
https://www.lintcode.com/problem/919/description

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
        res = max(res, count) #why maximum here
    return res


print(confRooms([(0, 30), (5, 10), (15, 20)]))
print(confRooms([(2, 7)]))