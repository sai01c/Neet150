"""
https://leetcode.com/problems/implement-stack-using-queues/

Approach - For stack we need to pop the top most element. We can achieve this through queue by popping all the element left to the top most element 
and appending it to the end. Then we pop the last leftmost element which will be the top most element. 

tc - O(n)
sc - O(n)
"""

class MyStack:

    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.q) - 1): #pop all left elements except the last element
            val = self.q.popleft()
            self.q.append(val)
        return self.q.popleft() #pop last left element

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
        
