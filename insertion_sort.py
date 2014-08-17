#sorting program using selection sorting method - Vivi

def insertion_sort(lst):
    """
    input: unsorted list
    output: sorted list
    
    sorting the list by dividing into 2 portions, sorted and unsorted
    and insert each element of the unsorted portion into the appropraite
    postion of the sorted portion until the list is completely sorted.
    """
    
    
    for idx in range(len(lst)):
        # jdx is the index of the element to be insert which
        # lies at the beginning of the unsorted portion
        # idx is the index of the element which is the last
        # element of the sorted portion
        jdx = idx
        element = lst[idx]
        # while the element to be insert is smaller than
        # the preceding element, swap their postion.
        while lst[jdx-1] > element and jdx > 0:
            lst[jdx] = lst[jdx-1]
            # continue decrementing until jdx reaches zero
            # this means that the inserting element has now
            # found the correct position
            jdx -= 1
        #now set the inserted element to be the last element
        # of the sorted portion
        lst[jdx] = element    
    return lst