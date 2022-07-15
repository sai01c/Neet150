"""
https://leetcode.com/problems/car-fleet/

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Approach: we want to check if the elements reach target so we come in the reverse direction
sort the elements based on position. 
calculate time for each element
based on speeds, if s1 < s2 then they form a fleet
"""

from tkinter import W


def carFleet(t, p, s):
    dic = {}
    for i in range(len(p)):
        dic[p[i]] = s[i]
    dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)

    stack = []
    for p, s in dic:
        time = (t - p) / s
        stack.append(time)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
