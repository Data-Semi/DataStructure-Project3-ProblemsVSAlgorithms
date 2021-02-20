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

print(counting_sort([4,3,6,6,3,3])) # sould print: [3,3,3,4,6,6]