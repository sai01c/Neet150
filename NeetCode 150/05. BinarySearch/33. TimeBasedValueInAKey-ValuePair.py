"""
https://leetcode.com/problems/time-based-key-value-store/

Approach: create a dictionary - {key: [(value, timestamp), (value, timestamp)]}

Tc: O(logn) binary search 
Sc: O(n) creating dictionary

"""


class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        
        #better to copy dic.values() to a new array for easy accessing
        if key in self.dic:
            values = self.dic[key]
        else:
            values = []
        res = ""  #initate res with empty string. if there's no answer we return empty string   
        
        #now do binary search on the length of the array
        #point to note is all the timestamps will be in sorted order so binary search works

        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            #we need to find the min timestamp available
            #if our target timestamp is less that means it is not min so we shift the pointers
            if timestamp < values[mid][1]:
                right = mid - 1
            
            #our target is more than current so we found minimum update res and continue
            elif timestamp >= values[mid][1]:
                res = values[mid][0]
                left = mid + 1
        
        return res
