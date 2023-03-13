"""
https://leetcode.com/problems/top-k-frequent-elements/

Approach: first, use a count dictionary i.e element:frequenctcount
now, sort them in decreasing order of count
now iterate through the sort list and append the key i.e element

Tc: O(n logn) sorting the dictionary based on counts. 
Sc: O(n) using dictionary and res array

Follow up O(n) solution
#worst case it could be n^2 also ?
instead of creating a frequency dictionary and sorting it.
create an array which has the frequency of elements.

"""

def func(nums, k):
    res = []
    freArray = [[] * len(nums)+1]
    count = Counter(nums)
    for num, fre in count.items():
        freArray[fre].append(num)
    for array in range(len(freArray)-1, -1, -1):
        for i in array:
            res.append(i)
            if len(res) == k:
                return res
