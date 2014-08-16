#selection sorting program - Vivi

def selection_sort(lst):
    """
    input: unsorted list
    output: sorted list
    
    sorting the list by dividing it to 2 portion, the sorted
    and the unsorted, in each iteration, look for the minimum in 
    the unsorted list and place it at the end of the sorted portion,
    repeat until sorting complete.
    """
    itr = len(lst)
    
    for idx in range(itr):
        #assign the current index value as the smallest so far
        smallest = lst[idx]
        for jdx in range(idx+1, itr):
            #if smaller number is found, reassign to be the smallest
            if lst[jdx] < smallest:
                smallest = lst[jdx]
            #if the smallest is not the one at the current index
            #of the iteration, swap their possition.    
            if lst[idx] != smallest:
                lst[idx], lst[jdx] = smallest, lst[idx]
            
    return lst                
                
                