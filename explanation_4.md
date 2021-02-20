# Dutch National Flag Problem

## Problem description

This problem given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Program description  

This program sorts the array in a single traversal.  
The idea is keep track of the index after the tail position(final index) of 0, the index infront of the head position of 2 and the current index of traverse.  
Every time if the element in current index is 0, it will switch with the element right after the tail position of 0.  
Every time if the element in current index is 2, it will switch with the element in front of head position of 2.

## Time compexity

Becaus of all operations takes constant time, and there is only one traverse. Therefore, the program's time complexity is O(n).

## Space complexity  

Because there is no extra space uses other than the input array,the space complexity is O(1). 
