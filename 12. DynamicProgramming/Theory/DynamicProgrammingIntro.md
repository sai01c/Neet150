# Dynamic Programming Intro

## Greedy vs DP

- both are solving optimization problems.
- strategy different purpose same. 
- optimization problems - we need to find minimum or maximum
- Greedy is pre determined approach. Approach is optimal so 
we use this approach. Eg: Djikstra's, Krusal's MST.
- DP, we find out all solutions and choose optimal solution.
- we mostly used recursion for DP
- Greedy, we decide only in the initial step but in DP, we decide
each and every step. 

## Tabulation

- This is done iteratively. 
- This is bottom up approach. We are going to solve from base case to required case.
- Generally, space complexity is better than memoization because we are not using recursion so no stack space.
- Instead of using array, if you use pointer's to store then you can decrease the space as well.


## Memoization

- We avoid repeated calls by storing the results of the recursive calls in an array. 
- This helps in reducing the time complexity.
- This follows top down approach - from required case to base case
