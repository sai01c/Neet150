## Map

- Unique keys
- keys are not sorted. 
- To sort them, you need to copy to a fresh list
- In dic, we can only have immutable data type as keys - int , string , tuple
- Search O(1)
- In python, dictionary doesn't store the order. So, if you want to sort them copy to a list while sorting it. 
```sortedCount = sorted(dict.items(), key = lambda x: x[1], reverse = True)```

## DefaultDict

- If the key is missing it doesn't return missing error. default dict is mainly used to skip the initializing dict part. 
- It creates the default paramter that is passed. defaultdict(list) creates []
- We can also create defaultdict(int) or float or set etc

```
d = defaultdict(set)
d["key"].add(2)
d["key"].add(2)

print(d) #defaultdict(<class 'set'>, {'key': {2}})

```

```
d = defaultdict(list)
d["key"].append(2)
d["key"].append(2)

print(d) #defaultdict(<class 'list'>, {'key': [2,2]})
```

## Counter


## Set

- Unique elements
- Search O(1)
- Insert O(1)
- Delete O(1)
- len(set) O(1)

## Array

- Insertion O(n)
- Inserting at end = O(1)
- Deletion O(n)
- deleting at end O(1)
- Searching O(n)
- Access O(1)



### Hashing

- Constant time search/lookup.
- value => hash-value
- we can search for the value in linear time by indexing using the hash-value.

### Collisions

- Same hash-value for 2 different input values.

1. Change the hash-function
2. Store multiple hash-values for a single input value using buckets and create new hash-function for each bucket.

- Both approaches are not ideal.
- Load Factor = number of inputs/ number of buckets.

### StringKeys

-
