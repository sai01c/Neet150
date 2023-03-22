"""
https://leetcode.com/problems/car-fleet/

Approach: we want to check if the elements reach target so we come in the reverse direction
sort the elements based on position. 
calculate time for each element.
we need to pop the smallest time as small will merge to large time
based on speeds, if s1 < s2 then they form a fleet
"""

def carFleet(t, p, s):
    dic = {}
    for i in range(len(p)):
        dic[p[i]] = s[i]
    dic = sorted(dic.items(), key=lambda x: x[0], reverse=True) #sort based on position in decresing order

    stack = []
    for p, s in dic:
        time = (t - p) / s
        stack.append(time)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop() #we want to pop the sortest time. 
            #longest time should be remaining in the stack as short will merge into long
    return len(stack)
