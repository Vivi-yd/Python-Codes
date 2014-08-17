#bubble sorting program - vivi

def bubble_sort(lst):
    """
    Input: an unsorted list
    Output: sorted list
    
    sort the list by comparing 2 adjacent elements of the list 
    at a time, swap their position if the left is greater than the 
    right from beginning till end, repeat until no element on 
    the left is greater than those on the right. 
    """
    cycle = len(lst)
   
    while cycle > 0:
        for idx in range(cycle-1):
           if lst[idx] > lst[idx+1]:
               lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
       
        cycle -= 1
    
    return lst
    

                                                                                            
                  