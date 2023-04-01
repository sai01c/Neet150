"""

https://leetcode.com/problems/baseball-game/

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

EXPLANATION: As we want to add elements and get the last and last second element, we want to use stack
stack we can remove the last using pop FILO. 

TC: O(n) we are iterating once
SC: O(n) we are using stack here
"""


def baseball(input):
    res = []
    for i in input:
        if i == "+":
            res.append(res[-1]+res[-2])
        elif i == "D":
            res.append(2*res[-1])
        elif i == "C":
            res.pop()
        else:
            res.append(int(i))
    return sum(res)


print(baseball(["5", "2", "C", "D", "+"]))
