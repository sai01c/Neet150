# Takeaways from Blind 75

- Counter is basically a dictionary. In python, dictionary doesn't store the order. So, if you want to sort them copy to a list while sorting it. `sortedCount = sorted(dict.items(), key = lambda x: x[1], reverse = True)`
- If the problem is about frequency, use dictionary.
- If the problem is about duplicate, use set.
- Sorted input - binary search
- For while loop, always make the computation inside the while loop.

  ```
  while left<right:
    mid = (left+right)//2
  ```

- For matrices, we always need to use two for loops

```
m = len(matrix) #number of rows
n = len(matrix[0]) #number of columns
for r in range(m):
  for c in range(n):
    matrix[r][c] #gives the element
```

- For matrices, common approach is to have 4 pointer's- left, right, top, bottom
- For matrices, when making operations always visulaize row and column and make the changes.
- comment down the co-ordinates for easy visualization
- For intervals, most of the cases we sort them. 
- Easier to use `for start, end in intervals` while iterating over them. 


