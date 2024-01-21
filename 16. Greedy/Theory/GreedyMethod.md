## Greedy Method

- one of the approach/ strategy to solve problems.
- optimization problems - which require either minimum result or maximum result.
- Each stage we make a decision to choose local minima/maxima which will result in global minima/maxima.
- Greedy never reconsiders it choices. DP does! 
- Problem should be in stages. Each stage we will consider one input from the problem. If it is feasible, we will include it in the optimal solution.

Example: 

1. Djikstra for minimum path

```
a = [1,2,3,4] n =4
Algo Greedy (a, n)

for num in array:
    x = select (num)
    if x is feasible:
        solution += x

```

![title](Images/Greedy.png)
