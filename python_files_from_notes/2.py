#!/usr/bin/env python
# coding: utf-8

# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.
# 
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example:
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
# 
# Here is some boilerplate code and test cases to start with:

# In[6]:


def rotated_array_search(start_i, input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)
    mid_i = length//2
    mid_e = input_list[mid_i]
    
    #base condition
    if length == 0:
        return -1
    if length == 1:
        if number == mid_e:
            return start_i + mid_i
        else:
            return -1
    
    L = input_list[:mid_i]
    R = input_list[mid_i+1:]
    
    if number == mid_e:
        return start_i + mid_i
    
    elif L[-1] > R[0]:  # both of L, R are not rotated array.
        # to find which sub array includes the number
        if number >= L[0] and number <= L[-1]:  #the number is in the range of L
            return start_i + binary_search(0,L, number)
        elif number >= R[0] and number <= R[-1]:  #the number is in the range of R
            start_i = start_i + mid_i+1
            return start_i + binary_search(0,R, number)
        else:
            return -1
        
    else:  # L[-1] < R[0]
        if L[0] > L[-1]:  # L is a rotated list, therefore, R is a sorted list
            if number >= R[0] and number <= R[-1]:  #search R
                start_i = start_i + mid_i+1
                return start_i + binary_search(0,R, number)
            else: # search L
                return start_i + rotated_array_search(start_i, L, number)  #call the function itself recursively
        
        else:  #L is not a rotated list, therefor, R is a rotated list
            if number >= L[0] and number <= L[-1]:  #the number is in the range of L
                return start_i + binary_search(0,L, number)
            else:
                return start_i + rotated_array_search(start_i, R, number)  #call the function itself recursively
            
    return -1

   
# binary search a number in a sorted input_list
#start_i keeps the position(first element's index) of sub array in the original "input_list" 
def binary_search(start_i, input_list, number):
    length = len(input_list)
    mid_i = length//2
    mid_e = input_list[mid_i]
    # base condition
    
    if length == 0:
        return -1
    if length == 1:
        if number == mid_e:
            return start_i + mid_i
        else:
            return -1
    # early stop condition
    if number > input_list[-1] or number < input_list[0]:
        return -1
    
    
    if number == mid_e:
        return start_i + mid_i
    elif number <  mid_e: 
        return binary_search(start_i, input_list[:mid_i], number)  # go to left side 
    else:
        start_i = start_i + mid_i + 1
        return binary_search(start_i, input_list[mid_i+1:], number)  # go to right side

    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(0,input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# ## Program description  
# The function`rotated_array_search` and `binary_search` are recursion function.
# `binary_search` is used for a sorted, non-rotated array.
# 
# 
# ## Time complexity  
#   
# `rotated_array_search` includes 2 parts. 
# One part is the dividing part, which is dividing the input array to sub-array. Every time recursively calls the function `rotated_array_search`, the searching area will be sized down to half of its original area. This means the time complexity is O(log(n)).
# 
# Another part is the searching part, which is searching the inputted number in a sorted array. This part is implemented by call function `binary_search`. Every time recursively calls the function `binary_search`, the searching area will be sized down to half of its original area. This means the total time complexity is O(log(n)).
# 
# All other operations take constant time, which has time complexity O(1). 
# Therefore, `rotated_array_search` has time complexity of O(log(n)).
# 
# ## Space complexity  
# The recursive function will take extra memory for executing the call stack. the call stack depth will be maximumly log(n).
# Because all the dividing and searching is done in the inputted array space, therefore, the space complexity of this program is O(log(n))
