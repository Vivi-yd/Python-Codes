
def bi_search(lst, k):
    """
    a function that return T/F on whether the value k
    is found in the list lst using binary search method
    Only work if lst is sorted
    """
    
    # compute midpoint of the list
    mid = len(lst)/2
    
    # length of list is 1, return whether that value is k
    if len(lst) == 1:
        return lst[0] == k
    
    # if the length of list is greater than 1, execute a 
    # recursive mechanism to check for value k
    else:
        if k < lst[mid]:
            return bi_search(lst[:mid], k)
        else:
            return bi_search(lst[mid:], k)
        


def bi_search2(lst, low, high, k):
    """
    a function that search whether value k is in the list lst
    within the lower bound low, and upper bound high.
    """
    # terminate if lower bound exceed upper bound
    if low > high:
        return False
    
    # check for the value when the length is only 1 
    if low + 1 == high:
        return lst[low] == k
    
    # compute midpoint of the list between the lower
    # and upper bound
    mid = (low + high)/2
    
    # if the length of list is greater than 1, execute a 
    # recursive mechanism to check for value k 
    
    if k < lst[mid]:
        return bi_search2(lst, low, mid, k)
    else:
        return bi_search2(lst, mid, high, k)
    


#link: http://www.codeskulptor.org/#user36_RhbCBymus9_5.py

    
