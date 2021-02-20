#!/usr/bin/env python
# coding: utf-8

# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
# 
# Bonus Challenge: Is it possible to find the max and min in a single traversal?

# In[15]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None
    
    min_e = ints[0]
    max_e = ints[-1]
    for e in ints:
        if isinstance(e, int) == False:  # if the list includes non-integer number, do not find min, max 
            return None,None
        if e < min_e:
            min_e = e
        if e > max_e:
            max_e = e
    return min_e, max_e

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([0.5, 2.5, 6])) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail")


# In[14]:


type(1) == "int"


# ## Question
# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

# In[2]:


print(l)


# ## Answer
# Yes, if I sacrifise space complexity.   
# In the first time, I will find a min and max in a single traversal. This will take time complexity of O(n).  
# Make an count array `count_array`.length is equal to max.(if the min is a big number, I can choose to set length of the `count_array` as max-min+1 to save space.)  
# I will travers the Unsorted array again, increase the element of `count_array[e]`. The index e is the element of Unsorted array. This will take time complexity of O(n).  
# Finally I will create a new array according to the count_array. This will take time complexity of O(n).
# Therefore, the total time complexity is O(n).  
# You can see my code as below.  
# 

# In[9]:


def counting_sort(ints):  # e.g. ints == [4,3,6,6,3,3]
    max_e = get_min_max(ints)[1]  # 6
    count_array = [0] * (max_e+1)  #[0,0,0,0,0,0,0]
    result = []
    for e in ints:
        count_array[e] += 1  # [0,0,0,3,1,0,2]
    for i,counted in enumerate(count_array):
        if counted != 0:
            result.extend([i] * counted)
    return result

        
        


# In[10]:


counting_sort([4,3,6,6,3,3])


# ## Program description  
# Max and Min in an Unsorted Array In this problem, we will look for the smallest and largest integers from a list of unsorted integers. 
# The function `get_min_max` can find the max and min of an integer array in a single traversal without use Python's inbuilt functions.
# 
# Sorting usually requires O(n log n) time, but the function `counting_sort` can sort an integer array with a time complexity of O(n).
# The condition is: The array should include integer(>=0) only.
# 
# For the first time, `counting_sort` finds a min and max in a single traversal. This will take time complexity of O(n).
# Make a count array `count_array`. length is equal to max.(if the min is a big number, I can choose to set the length of the `count_array` as max-min+1 to save space complexity.)
# After this, the program traverses the Unsorted array again, increase the element of count_array[e] accordingly. The index e is the element of the Unsorted array. This will take time complexity of O(n).
# Finally, a new array is created according to the `count_array`. This will take time complexity of O(n). Therefore, the total time complexity is O(n).
# 
# ## Time compexity
# The function `get_min_max` performs only one traversal of the input array, therefore, the code should run in O(n) time.
# The function `counting_sort` has a time complexity of O(n), I have described above. 
# 
# ## Space complexity  
# Because all space uses in function `get_min_max` is the constant size and not impacted by the input list, the space complexity is O(1).
# The function `counting_sort` has space complexity O(n), because of the extra space uses by the `count_array` and `result`.In the worst case, the space complexity will be O(2n).
# 

# In[ ]:




