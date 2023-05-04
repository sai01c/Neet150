"""
https://leetcode.com/problems/implement-queue-using-stacks/

approach - we use two stacks to implement queue.
let us say we have to build a queue of [1,2,3,4] queue pop is 1.
so we pop all the elements to right of 1 from our stack and add these elements to another stack then [4,3,2]
return the last stack element - 1
now, pop all the elements from second stack and append them back to initial stack then [2,3,4]

tc - O(n)
sc - n
"""

class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            val = self.stack.pop()
            self.temp.append(val)
        ans = self.stack.pop()
        
        for i in range(len(self.temp)):
            val = self.temp.pop()
            self.stack.append(val)
        return ans
    
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
