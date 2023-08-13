"""
https://leetcode.com/problems/group-anagrams/

Approach: to have count dictionary in count {key : value} key is the sorted word, values are the anagrams
so we iterate over the each word check if the anagrams is in count and append it. 

Tc: O(n^2 logn) we are iterating over the count dictionary . 
Sc: O(n) we are using count dictionary

"""

def group(strs):
    count = {}
    res = []
    for word in strs:
        sortWord = "".join(sorted(word)) #this is n logn operation
        if sortWord not in count:
            count[sortWord] = [word]
        else:
            count[sortWord].append(word)
    for val in count.values():
        res.append(val)

    return res


def func(strs):
    dic = defaultdict(list)
    for string in strs:
        count = [0] * 26 #this array will have frequencies in alphabetical order
        for char in string:
            count[ord(char) - ord('a')] += 1
        dic[tuple(count)].append(char)
        #we are changing from list to tuple because it is immutable
        #in dic we can only have immutable data structures as keys
        #eg - int, string, tuple
    return dic.values()

"""
Tc: O(26n)
Sc: O(n)
"""