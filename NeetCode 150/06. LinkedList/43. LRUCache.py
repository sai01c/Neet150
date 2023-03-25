"""
https://leetcode.com/problems/lru-cache/

Approach: we will create double linked list so it is easy to maintain the least recently used
node. we will update the linked list from right. LRU will be the left. 
we use two functions delete and insert. we always delete and insert for all methods just to
maintain LRU

Tc O(1) get and put
Sc O(n) map, linked list
"""

class Node:
    def __init__(self, key, val): 
    #initiate node class with next and prev pointers, key and value.
        self.key = key 
        self.val = val
        self.next = self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {} #key is key, val is Node

        self.left = Node(0, 0) #creating double linked list with left and right pointers
        self.right = Node(0, 0)

        self.left.next = self.right #both pointing to each other
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.dic:
            self.delete(self.dic[key]) #deleting from linked list
            self.insert(self.dic[key]) #inserting to linked list
            return self.dic[key].val 
        return -1

    def insert(self, node): #use right as next node and right.prev as previous node
        pre = self.right.prev #insert new node b/w them and connect pointers.
        nxt = self.right
        node.next = nxt
        node.prev = pre
        pre.next = node
        nxt.prev = node
    
    def delete(self, node):
        pre = node.prev #deleting that node
        nxt = node.next #take the pointer of previous and next nodes and connect them
        pre.next = nxt
        nxt.prev = pre

        
    def put(self, key: int, value: int) -> None:
        if key in self.dic: #if key is there, we delete that Node
            self.delete(self.dic[key])
        self.dic[key] = Node(key, value) #inserting key as key, node as value of dic.
        self.insert(self.dic[key]) #inserting to linked list

        if len(self.dic) > self.cap: #if we exceed capacity delete LRU
            lru = self.left.next
            self.delete(lru) #delete from linked list
            del self.dic[lru.key] #delete from dict

        



