# Rearrange Array Elements

## Problem description

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Program description  

The idea is sorting the elements and put them into 2 arrays by order.  
The steps are as below.  
Step1: Make 2 empty arrays, array0, array1.  
Step2: Find the maximum element from `input_list`, put it to array0.  
Step3: Find the maximum element from the rest of `input_list`, put it to array1.  
Step4: Repeat Step2, Step3 until final element of `input_list`.  
Step5: Combine elements in array0 to an integer. Do the same thing to array1.  

If I sort the `input_list` and make array1, array2 similar to Step2, Step3 above, I need to go through all elements after the sort.  
This means I need extra time complexity O(n). Because "Merge sort" takes O(nlog(n)), "Quick sort" takes O(nlog(n)) in a good pivot(we need to use extra O(n) to choose the best pivot), I decided to not use this method.  

Instead of the "sort first" solution, I choose to use heapsort to get the maximum element every time. and pop the maximum element to array0, array1.

## Time compexity

The function `rearrange_digits` is a heapsort function plus Step2-Step4 above.  
Because the funciton `heapify` has time complexity of O(log(n)), and I need to do `heapify` every time after I get the maximum element in a subtree. This means I need to do n time of `heapify`. Therefore, my program has time complexity of O(nlog(n)).  

## Space complexity  

Because of all space uses in this program is constant size and not impacted by the input list, the space complexity is O(1). 
