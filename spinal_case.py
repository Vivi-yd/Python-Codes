
def spinal_case(aString):

	"""
	this function coverts a string of expressions to a string of the same expressions
	but written in spinal case, which means expressions are linked with dashes in between.

	Input: a string
	Output: a-string
	"""

	# spliting the string into a list of expressions
	list_of_expressions = aString.split() 
	
	length = len(list_of_expressions)

	spinal_string = ""

	if length == 0:
		return aString

	for idx in range(length-1):
		spinal_string += list_of_expressions[idx] + "-"

	spinal_string += list_of_expressions[length-1]	


	return spinal_string



x = "I love python"
z = "I love you very much"
mix_list = "a b c 89kh d;ajdi; dww "
empty = ""
print spinal_case(x)
print spinal_case(y)
print spinal_case(z)
print spinal_case(mix_list)
print spinal_case(empty)