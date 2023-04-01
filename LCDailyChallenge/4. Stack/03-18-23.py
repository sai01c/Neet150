"""
https://leetcode.com/problems/design-browser-history/

Approach: we can use stack to maintain the history as it is go back using stack.
we also need to main a counter to see the current
there are few edge cases here - 

while going forward or back if our pointer exceeds the length of stack return the top or bottom element.
while visiting an element we need to make the current point at this element and remove elments above this index in the stack.

"""

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.stack.append(homepage)
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr >= len(self.stack): #means we want to insert new element
            self.stack.append(url)
        
        else: #we want to insert element to the exisiting index
            while len(self.stack) > 1 + (self.curr): 
                self.stack.pop() #we want to remove elements more than that index
            self.stack[self.curr] = url

    def back(self, steps: int) -> str:
        while steps > 0:
            steps -= 1
            self.curr -= 1
        
        if self.curr < 0: #if we went below stack
            self.curr = 0
        return self.stack[self.curr]

    def forward(self, steps: int) -> str:
        while steps > 0:
            steps -= 1
            self.curr += 1

        if self.curr >= len(self.stack): #if we forwarded above stack
            self.curr = -1
        
        return self.stack[self.curr]
