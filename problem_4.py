def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    pos = 0  #index of current judgement position
    next_0 = 0  # index of next possible insert position of 0
    next_2 = len(input_list)-1  # index of next possible insert position of 2
    
    if next_2 == -1 or next_2 == 0:  # empty list, or a list has only 1 element 
        return input_list  # return itself
    
    while pos <= next_2:
        if input_list[pos] == 0:
            input_list[next_0], input_list[pos] = input_list[pos], input_list[next_0]
            next_0 += 1
            if pos < next_0:  # pos and next_0 was in the same position
                pos += 1
        elif input_list[pos] == 2:
            input_list[next_2], input_list[pos] = input_list[pos], input_list[next_2]
            next_2 -= 1
        else:  # it is 1, move to next
            pos += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])