def read_file():
    """
    open and read file given for assignment two
    and return an array of a list of integers in the file
    """
    
    thefile = open('C:/Documents and Settings/steven/repos/Python-Codes/Algo_One_Stanford/assignment_2_QuickSort.txt'
, 'r')
    
    # initializing the array to be returned
    array = []
    
    
    for line in thefile:
        
        # only take entries that has length greater than zero
        if len(line[:-1]) != 0:
            array.append(int(line[:-1]))
            
    return array
    

            
#### for problem no.1 : counting no. of comparisons when first element is
#### always chosen as pivots.

# initializing global variable for no. of comparisons
comparisons_1 = 0
                                    
def quicksort_one(array):
    
    """
    a divide and conquer sorting algorithm that sort an 
    array in ascending order by choosing the first element
    as pivot and partitioning the array
    
    input: any array with length n
    output: sorted array
    """
    
    n = len(array)
    
    # keeping track the number of comparisons made between the 
    # pivot and other elements in the array during the whole sorting process.
    global comparisons_1
    
    # base case
    if n < 2:
        return array
    
    # recursive case
    else:
        # always choose the first element as pivot
        pivot = array[0] 
        
        
        # idx keep track of the border between
        # elements smaller than pivot and those greater than pivot
        idx = 1
        
        # jdx keep track of the border between partitioned part
        # and unpartitioned part
        for jdx in range(idx, n):
            
            # increment comparision
            comparisons_1 += 1
            
            # the current checking element smaller than pivot
            if array[jdx] < pivot:
                
                # swap position with the idx element
                array[jdx], array[idx] = array[idx], array[jdx]
                # increment idx by one
                idx += 1                

        # place the pivot at the correct (final) position
        array[0], array[idx-1] = array[idx-1], array[0]
        
        #recursively using quicksort on part left and right of pivot
        return quicksort_one(array[:idx-1]) + [pivot] + quicksort_one(array[idx:])
        
         


the_array = read_file()

quicksort_one(the_array)
print comparisons_1                                           
                                            
 
 
#### for problem no.2 : counting no. of comparisons when last element is
#### always chosen as pivots. 

comparisons_2 = 0
                                    
def quicksort_two(array):
    
    """
    a divide and conquer sorting algorithm that sort an 
    array in ascending order by choosing the last element
    as pivot and partitioning the array
    
    input: any array with length n
    output: sorted array
    """
    
    n = len(array)
    
    # keeping track the number of comparisons made between the 
    # pivot and other elements in the array during the whole sorting process.
    global comparisons_2
    
    # base case
    if n < 2:
        return array
    
    # recursive case
    else:
        # always choose the first element as pivot
        pivot = array[-1] 
        
        # swap position of the pivot with the first element
        array[0], array[-1] = pivot, array[0]
        
        # idx keep track of the border between
        # elements smaller than pivot and those greater than pivot
        idx = 1
        
        # jdx keep track of the border between partitioned part
        # and unpartitioned part
        for jdx in range(idx, n):
            
            # increment comparision
            comparisons_2 += 1
            
            # the current checking element smaller than pivot
            if array[jdx] < pivot:
                
                # swap position with the idx element
                array[jdx], array[idx] = array[idx], array[jdx]
                # increment idx by one
                idx += 1                

        # place the pivot at the correct (final) position
        array[0], array[idx-1] = array[idx-1], array[0]
        
        #recursively using quicksort on part left and right of pivot
        return quicksort_two(array[:idx-1]) + [pivot] + quicksort_two(array[idx:])
        
         


the_array = read_file()

quicksort_two(the_array)
print comparisons_2                                           
                                            
        
#### for problem no.3 : counting no. of comparisons when the "Median of Three"
#### rule is used to choose pivots. 

from math import ceil

comparisons_3 = 0
                                    
def quicksort_three(array):
    
    """
    a divide and conquer sorting algorithm that sort an 
    array in ascending order. The "median of three" (median of the first, last and
    the median of the element) is used to choose the pivot.
    
    input: any array with length n
    output: sorted array
    """
    
    n = len(array)
    
    # keeping track the number of comparisons made between the 
    # pivot and other elements in the array during the whole sorting process.
    global comparisons_3
    
    # base case
    if n < 2:
        return array
    
    # recursive case
    else:
        #initialize a list to store the 3 elements that the pivot will be chosen from.
        pivot_candidates = []
        
        # find the index of the median element
        med_index = (int(ceil(n/2.0))-1)
        # put the first, last and the middle element into the list
        pivot_candidates.append(array[0])
        pivot_candidates.append(array[-1])
        pivot_candidates.append(array[med_index])
        
        # sort the the list
        sorted_candidates = sorted(pivot_candidates) # i know this is not a good idea...
        
        # always choose the middle element of the list as pivot
        pivot = sorted_candidates[1] 
        
        # find the pivot index
        
        if pivot == array[0]:
            pivot_index = 0
            
        elif pivot == array[-1]:
            pivot_index = -1
        
        else:
            pivot_index = med_index
        
        # swap position of the pivot with the first element
        array[0], array[pivot_index] = pivot, array[0]
        
        # idx keep track of the border between
        # elements smaller than pivot and those greater than pivot
        idx = 1
        
        # jdx keep track of the border between partitioned part
        # and unpartitioned part
        for jdx in range(idx, n):
            
            # increment comparision
            comparisons_3 += 1
            
            # the current checking element smaller than pivot
            if array[jdx] < pivot:
                
                # swap position with the idx element
                array[jdx], array[idx] = array[idx], array[jdx]
                # increment idx by one
                idx += 1                

        # place the pivot at the correct (final) position
        array[0], array[idx-1] = array[idx-1], array[0]
        
        #recursively using quicksort on part left and right of pivot
        return quicksort_three(array[:idx-1]) + [pivot] + quicksort_three(array[idx:])
        
         


the_array = read_file()

quicksort_three(the_array)
print comparisons_3 
                     

                                            