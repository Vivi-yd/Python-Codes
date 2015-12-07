#python implementation of selection sort

from random import randint

def selection_sort(aList):

	"""
	this is a sorting function where a list of item is sorted in ascending order
	by spliting into 'sorted' section and the 'unsorted' section.
	The function stops when the 'unsorted' section is empty.

	Input: a list (sorted or unsorted)
	Output: a sorted list in ascending order

	"""

	for i in range(0, len(aList)):
		min_val = aList[i] # first element of the unsorted portion
		min_val_index = i

		for j in range(i+1, len(aList)):

			if min_val > aList[j]:

				min_val_index = j

				min_val = aList[j]

		if i != min_val_index:		
			aList[i], aList[min_val_index] = aList[min_val_index], aList[i]
	
	print "sorted list: ", aList	
	return aList


for test_count in range(10):
	x = [randint(-100, 100) for x in range(randint(0, 10))]
	print "original list: ", x
	selection_sort(x)
