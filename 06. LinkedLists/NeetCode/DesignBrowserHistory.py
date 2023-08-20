"""
https://leetcode.com/problems/design-browser-history/

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode(0)
        self.right = ListNode(0)
        home = ListNode(homepage)
        self.curr = home
        self.left.next = self.curr
        self.curr.prev = self.left
        self.curr.next = self.right
        self.right.prev = self.curr

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.right.prev = node
        node.next = self.right
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr and self.curr.prev and steps:
            steps -= 1
            self.curr = self.curr.prev
        if self.curr == self.left:
            self.curr = self.curr.next
        return self.curr.val
    
    def forward(self, steps: int) -> str:
        while steps and self.curr and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        if self.curr == self.right:
            self.curr = self.curr.prev
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)