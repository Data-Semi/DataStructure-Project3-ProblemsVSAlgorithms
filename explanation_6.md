# Max and Min in a Unsorted Array

## Problem description

Max and Min in a Unsorted Array In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

## Program description  

Max and Min in an Unsorted Array In this problem, we will look for the smallest and largest integers from a list of unsorted integers. 
The function `get_min_max` can find the max and min of an integer array in a single traversal without use Python's inbuilt functions.

Sorting usually requires O(n log n) time, but the function `counting_sort` can sort an integer array with a time complexity of O(n).
The condition is: The array should include integer(>=0) only.

For the first time, `counting_sort` finds a min and max in a single traversal. This will take time complexity of O(n).  
Make a count array `count_array`. length is equal to max.(if the min is a big number, I can choose to set the length of the `count_array` as max-min+1 to save space complexity.)  
After this, the program traverses the Unsorted array again, increase the element of count_array[e] accordingly. The index e is the element of the Unsorted array. This will take time complexity of O(n).  
Finally, a new array is created according to the `count_array`. This will take time complexity of O(n). Therefore, the total time complexity is O(n).  

## Time compexity

The function `get_min_max` performs only one traversal of the input array, therefore, the code should run in O(n) time.  
The function `counting_sort` has a time complexity of O(n), I have described above. 

## Space complexity  

Because all space uses in function `get_min_max` is the constant size and not impacted by the input list, the space complexity is O(1).  
The function `counting_sort` has space complexity O(n), because of the extra space uses by the `count_array` and `result`.In the worst case, the space complexity will be O(2n).
