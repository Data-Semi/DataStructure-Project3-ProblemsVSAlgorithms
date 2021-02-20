# Finding the Square Root of an Integer

## Problem description

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

## Program description  

The function`sqrt_small` is a recursion function.

## Time complexity  

All operations takes O(1) time.   
Every time recursively call the function `sqrt_small`, the searching area will be sized down to the half of its original area.  
This means the total time complexity is O(log(n)).

## Space complexity  

The recursive function will take extra memory for executing the call stack. the call stack depth will be maximumly log(n), therefore, the space complexity of this function is O(log(n))
