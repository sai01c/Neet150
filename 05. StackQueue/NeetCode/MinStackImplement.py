"""
https://leetcode.com/problems/min-stack/

Approach: for push and pop operations we can directly use the built-in functions. 
for minimum and top we can not use the same stack. 
So, we use a different stack where we push only the minimum values

Tc: O(1)
Sc: O(n) as using stack
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        self.stack[-1]

    def getMin(self) -> int:
        self.minStack[-1]

