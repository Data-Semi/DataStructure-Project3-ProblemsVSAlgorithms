#!/usr/bin/env python
# coding: utf-8

# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
# 
# for e.g. [1, 2, 3, 4, 5]
# 
# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
# 
# Here is some boilerplate code and test cases to start with:

# In[65]:


def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subtree
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
    
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index) 
        
def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr) 
    # edge case , returns -1
    if n <=1:
        return -1,-1
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)  # from leaf to root, this means, every sub-tree always has been sorted during build up.
    array0 = []
    array1 = []
    # One by one extract elements 
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
        if i % 2 == 0:
            array0.append(arr[i])
        else:
            array1.append(arr[i])
            
    res0 = int("".join(map(str, array0)))
    res1 = int("".join(map(str, array1)))
    return res0, res1


# In[66]:


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6], [4, 6]])
test_function([[4], [-1,-1]])  #edge case, only 1 element has been given. return -1,-1 
test_function([[], [-1,-1]])  #edge case, only 1 element has been given. return -1,-1


# ## Program description  
# The idea is sorting the elements and put them into 2 arrays by order.
# The steps are as below.
# Step1: Make 2 empty arrays, array0, array1.
# Step2: Find the maximum element from `input_list`, put it to array0.
# Step3: Find the maximum element from the rest of `input_list`, put it to array1.
# Step4: Repeat Step2, Step3 until final element of `input_list`.
# Step5: Combine elements in array0 to an integer. Do the same thing to array1.
# 
# If I sort the `input_list` and make array1, array2 similar to Step2, Step3 above, I need to go through all elements after the sort.
# This means I need extra time complexity O(n). Because "Merge sort" takes O(nlog(n)), "Quick sort" takes O(nlog(n)) in a good pivot(we need to use extra O(n) to choose the best pivot), I decided to not use this method.
# 
# Instead of the "sort first" solution, I choose to use heapsort to get the maximum element every time. and pop the maximum element to array0, array1.
# 
# ## Time compexity
# The function `rearrange_digits` is a heapsort function plus Step2-Step4 above.
# Because the funciton `heapify` has time complexity of O(log(n)), and I need to do `heapify` every time after I get the maximum element in a subtree. This means I need to do n time of `heapify`. Therefore, my program has time complexity of O(nlog(n)).  
# 
# ## Space complexity  
# Because of all space uses in this program is constant size and not impacted by the input list, the space complexity is O(1). 
# 

# In[ ]:




