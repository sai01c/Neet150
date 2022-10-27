"""
https://leetcode.com/problems/daily-temperatures/

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Approach: we add the temp to a stack. 
Now if the incoming temp is more than stack temp we pop current and
get the diff of the index. 

Tc: O(n) only for loop
Sc: O(n) stack
"""


def dailytemp(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]: 
            #O(1) as just checking stack and comparing values
            #pop is also O(1)
            stackIndex, stackTemp = stack.pop()
            res[stackIndex] = index - stackIndex
        stack.append([index, temp])
    return res


print(dailytemp([73, 74, 75, 71, 69, 72, 76, 73]))
