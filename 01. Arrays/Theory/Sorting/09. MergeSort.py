# 2- way merge sort

arr1 = [1, 4, 3, 2]
arr2 = [3, 6, 8, 2]
new = [0, 0, 0, 0, 0, 0, 0, 0]

i = 0
j = 0
k = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        new[k] = arr1[i]
        i += 1
        k += 1

    elif arr1[i] > arr2[j]:
        new[k] = arr2[j]
        j += 1
        k += 1


while i < len(arr1):
    new[k] = arr1[i]
    i += 1
    k += 1

while j < len(arr2):
    new[k] = arr2[j]
    j += 1
    k += 1

print(new)
#[1, 3, 4, 3, 2, 6, 8, 2]

#Tc (nlogn)


# Merge Sort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        mergeSort(arr1)
        mergeSort(arr2)

        i, j, k = 0, 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
                k += 1

            elif arr1[i] > arr2[j]:
                arr[k] = arr2[j]
                j += 1
                k += 1

        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1
    return arr


test = [1, 2, 3, 2, 5, 3, 8, 6, 2, 1]
print(mergeSort(test))

"""
Pro's of merge sort- 

useful for very large list
useful for linked list
external sorting- external means data is stored externally (not RAM)
stable - order of duplicate elements is maintained. 

con's of merge sort- 

in place sorting is not done. extra space is needed
for small data- insertion sort is better

merge sort O(nlogn)
quick sort O(n^2)
bubble sort O(n^2)

"""
"""
# Merge Sort

- Divide and Conquer algorithm
- **_TC O(nlogn)_**
- **_SC O(n)_**

```
left = [0:len(arr)/2]
right = [len(arr)/2:]
i = 0
j = 0
k = 0

while i < len(left) and j < len(right) > :
    if left[i] < right[j]:
        final[k] = left[i]
        i += 1
    else:
        final[k] = right[j]
        j += 1
k += 1
while i < len(left):
    final[k] = left[i]
    k += 1
    i += 1
while j < len(right):
    final[k] = right[j]
    j += 1
    k += 1
```

"""
