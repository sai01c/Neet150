"""

https://leetcode.com/problems/seat-reservation-manager/

"""

class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.heap = []
        self.visit = set()
        for i in range(1, n+1):
            heapq.heappush(self.heap, i)
        
    def reserve(self) -> int:
        
        while True:
            val = heapq.heappop(self.heap)
            if val not in self.visit:
                self.visit.add(val)
                return val
        

    def unreserve(self, seatNumber: int) -> None:
        self.visit.remove(seatNumber)
        heapq.heappush(self.heap, seatNumber)
        