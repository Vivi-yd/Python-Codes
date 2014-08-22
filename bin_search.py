# binary search program (using recursion)- Vivi

def bi_search(val, lst):
    """
    input: a given element and a SORTED list.
    output: True/False.
    
    a program that determine whether the given value val, is
    present in the list by binary search method: pick a middle
    value, compare it to val, if the val is greater, repeat
    the process to the right half, else repeat the process
    to the left half.
    continue this recursion until val found/not found.
    """
    # mid point of the list
    mid_idx = len(lst)/2
    
    # define base case of the recursive function
    if len(lst) == 1:
        return lst[0] == val
    
    # recursive case
    else:

        if val < lst[mid_idx]:
            return bi_search(val, lst[:mid_idx])
        
        else:
            return bi_search(val, lst[mid_idx:])
            