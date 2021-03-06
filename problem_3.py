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