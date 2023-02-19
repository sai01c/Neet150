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


print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))
