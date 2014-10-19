def create_array():
    """
    open, read and return a list of integers containing in the file give
    """
    
    thefile = open('C:/Documents and Settings/steven/repos/Python-Codes/Algo_One_Stanford/IntegerArray.txt'
, 'r')
    
    ans = []
    
    for line in thefile:
        if len(line[:-1])!= 0:
            ans.append(int(line[:-1]))
            
    return ans
    
        

def merge_and_count_splitInv(lst1, lst2):
    """
    helper function to count the number of split inversion in 2 arrays
    i.e. number of inversion across 2 lists.
    
    input 2 unsorted lists
    output a sorted list in ascending order 
    and the number of split inversions in the list
    """
    
    idx = 0 # idx for index of list 1
    jdx = 0 # jdx for index of list 2
    
    # initialize empty list to store sorted answer
    sorted_lst = []
    
    # number of split inversion
    
    split_inv_count = 0
    
    # loop ends whever one of the index 
    # reache the end of the list
    while idx != len(lst1) and jdx != len(lst2):
        
        # compare the element of corresponding indices
        # of both list and append the smaller one 
        # to the answer
        if lst1[idx] < lst2[jdx]:
            sorted_lst.append(lst1[idx])
            idx += 1
        else:
            sorted_lst.append(lst2[jdx])
            jdx += 1
            
            split_inv_count += len(lst1[idx:])
    
    # append remaining elements at the end of 
    # the sorted list if any is left.
    sorted_lst.extend(lst1[idx:])
    sorted_lst.extend(lst2[jdx:])
    
    return sorted_lst, split_inv_count


def sort_and_count(lst):
    """
    counting inversion using divide and conquer method,
    utilizing merge sort to keep track of pairs of numbers
    that are inverted
    """
    
    lst_len = len(lst)
    
    if lst_len == 1:
        return 0
    
    else:
        # count number of inversion in each half of the list
        inv_count1 = sort_and_count(lst[:lst_len/2])
        inv_count2 = sort_and_count(lst[lst_len/2:]) 
        
        # count number of inversion across the two halves
        split_inv = merge_and_count_splitInv(lst[:lst_len/2], lst[lst_len/2:])
    
    return inv_count1 + inv_count2 + split_inv[1]
    
                                                                    

textlist = create_array()

inversions= sort_and_count(textlist)

print inversions
    