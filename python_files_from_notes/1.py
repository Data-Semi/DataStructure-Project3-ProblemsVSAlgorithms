#!/usr/bin/env python
# coding: utf-8

# ## Finding the Square Root of an Integer<br>
# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
# 
# For example if the given number is 16, then the answer would be 4.
# 
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
# 
# The expected time complexity is O(log(n))
# 
# Here is some boilerplate code and test cases to start with:

# In[4]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #special condition, number == 0 or 1
    if number == 0:
        return 0
    if number == 1:
        return 1
    # the other conditions
    return sqrt_small(0, number, number)


def sqrt_small(start, end, number):

    #base condition
    if start == end:
        return start
    elif start +1 == end:
        return start
    else:
        mid = start + (end-start)//2
        if mid * mid > number:
            #go to left side
            return sqrt_small(start, mid, number)
        elif mid * mid < number:
            # go to right side
            return sqrt_small(mid, end, number)
        else:
            return mid
            
             

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# ## Program description  
# The function`sqrt_small` is a recursion function.
# 
# 
# ## Time complexity  
# All operations takes O(1) time.   
# Every time recursively call the function `sqrt_small`, the searching area will be sized down to the half of its original area.
# This means the total time complexity is O(log(n)).
# 
# ## Space complexity  
# The recursive function will take extra memory for executing the call stack. the call stack depth will be maximumly log(n), therefore, the space complexity of this function is O(log(n))
# 
