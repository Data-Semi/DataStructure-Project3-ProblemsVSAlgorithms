# Search in a Rotated Sorted Array

## Problem description

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## Program description  

The function`rotated_array_search` and `binary_search` are recursion function.  
`binary_search` is used for a sorted, non-rotated array.

## Time complexity  
  
`rotated_array_search` includes 2 parts. 
One part is the dividing part, which is dividing the input array to sub-array. Every time recursively calls the function `rotated_array_search`, the searching area will be sized down to half of its original area. This means the time complexity is O(log(n)).

Another part is the searching part, which is searching the inputted number in a sorted array. This part is implemented by call function `binary_search`. Every time recursively calls the function `binary_search`, the searching area will be sized down to half of its original area. This means the total time complexity is O(log(n)).

All other operations take constant time, which has time complexity O(1).  
Therefore, `rotated_array_search` has time complexity of O(log(n)).

## Space complexity  

The recursive function will take extra memory for executing the call stack. the call stack depth will be maximumly log(n).  
Because all the dividing and searching is done in the inputted array space, therefore, the space complexity of this program is O(log(n))
