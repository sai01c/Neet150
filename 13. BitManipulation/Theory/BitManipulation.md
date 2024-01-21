# Bit Manipulation

## Binary representation: 

- Just like how numbers we use 10 we need to use 2 for binary
- Eg: 6 - 
```
while number > 0:
    remainder = number % 2
    number = number // 2
    res += str(remainder)
```

## Addition

- Same like decimal addition but 2
- If total is 2 digit is 0 and carry is 1
- If total is 3 digit is 1 and carry is 1

## Subtraction 

- 2 - 1 can be written as 2 + (-1)
- So, find negation of number and add this number.

## Negative

- To get binary representation of negative numbers - First, get the binary
representation of positive number then invert all the numbers and add 1. 

 ## Bitwise Operators

 - AND - if 1 and 1 then 1 else 0
 - OR - if any 1 then 1 else 0
 - XOR - if only 1 then 1. else 0
 - Negation - Invert

 ## Shifting 

 - Left shifting - we shift the digits to left such that 0th index will be 
 removed and add one 0 to the right
 - Right shifting - we shift the digits to right such that n-1 element will be 
 removed and add one 0 to the left.
 - Left shift multiplies by 2
 - Right shift divides by 2