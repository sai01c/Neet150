"""
iterate through the first array and add elements to the set. 
Now, iterate through the second array and add elements to the set. 
set does not have duplicate elements. 
"""
res = set()


def union(arr1, arr2):
    for i in range(len(arr1)):
        res.add(arr1[i])
    for j in range(len(arr2)):
        res.add(arr2[j])
    return len(res)


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
print(union(arr1, arr2))
