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