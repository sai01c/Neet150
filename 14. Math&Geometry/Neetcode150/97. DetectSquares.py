"""
https://leetcode.com/problems/detect-squares/

APPROACH: add, count methods are given. 
For add method, we have a list of lists. This add method appends the list here. 
For count method, we maintain the counts of the points, we are doing this because 
we may have duplicate squares. we can have two points at same x and y cordinates. 
so here we can count two squares. 

TC: O(n) iterating through all the points once
SC: O(N) dict

"""

from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.count[tuple(point)] += 1 #we need to convert list to tuple to be able to add to dic
        self.points.append(point) #maintain an array that consists of all the points

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            
            if (
                (abs(py - y) != abs(px - x)) or #this is basically diagonal so it can't be different
                x == px or #if same point then we can't form a square
                y == py
                ):
                continue
            #then multiply the counts - because if two points same then we can get the count of 2 using multiply
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] 
        return res
