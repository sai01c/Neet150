"""

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
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
