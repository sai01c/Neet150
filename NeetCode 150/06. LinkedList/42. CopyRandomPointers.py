"""
https://leetcode.com/problems/copy-list-with-random-pointer/

Approach: first we need a dictionary. Whenever we are trying to clone something, we use dic
first, while iterating through the linkedlist, we create a copy of the value and add it to the dic
Now, use another while to iterate over the linkedlist and add next and random pointers by indexing the dic


Tc: O(n) while loop
Tc: O(n) dictionary
"""
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None:None}
        original = head
        while original:
            copy = Node(original.val)
            dic[original] = copy
            original = original.next
        
        original = head
        while original:
            copy = dic[original]
            copy.next = dic[original.next]
            copy.random = dic[original.random]
            original = original.next
        
        return dic[head]
        """
