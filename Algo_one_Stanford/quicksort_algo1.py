# quicksort implementation - Vivi

from random import randrange

def quicksort(array):
    
    """
    a divide and conquer sorting algorithm that sort an 
    array in ascending order by choosing random pivot 
    and partitioning the array
    
    input: any array with length n
    output: sorted array
    """
    
    n = len(array)
    
    # base case
    if n < 2:
        return array
    
    # recursive case
    else:
        # randomly choose an index in the array as pivot
        pivot_index = randrange(n)
        pivot = array[pivot_index] 
        
        # swap position of the pivot with the first element
        array[0], pivot = pivot, array[0]
        
        # idx keep track of the border between
        # elements smaller than pivot and those greater than pivot
        idx = 1
        
        # jdx keep track of the border between partitioned part
        # and unpartitioned part
        for jdx in range(idx, n):
            
            # the current checking element smaller than pivot
            if array[jdx] < pivot:
                
                # swap position with the idx element
                array[jdx], array[idx] = array[idx], array[jdx]
                # increment idx by one
                idx += 1                

        # place the pivot at the correct (final) position
        array[0], array[idx-1] = array[idx-1], array[0]
        
        #recursively using quicksort on part left and right of pivot
        return quicksort(array[:idx-1]) + [pivot] + quicksort(array[idx:]) 
        
L1 = [1, 4, 2, 8, 100, -38, 4, 5, 9, 1, 0, 2]
print quicksort(L1)        