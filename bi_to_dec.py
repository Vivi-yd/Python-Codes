
import unittest

def bi_to_dec(n):
	"""
	This funciton converts a binary number (compose of 1 & 0) to a decimal number

	Input: an integer in binary
	Output: an integer in decimal

	"""

	bi_num = str(n)

	# reverse the number for indexing purpose because the corresponding digit will 
	# be holding the digit of 2 to the power of that index
	rev_bi_num = bi_num[::-1] 
	print "reversed binary: ", rev_bi_num

 	length = len(bi_num)


 	# accumulator for the decimal number
	dec_num = 0

	# iterate over the length of the binary number, 
	# add 2 to the power of that index whenever a digit is found to be 1. 
	# Ignore when it's 0. 
	for idx in range(length):

		if rev_bi_num[idx] == "1":

			
			dec_num += 2**idx
			print "indexing at: ", idx
			print "current accumulated decimal: ", dec_num

	return dec_num



class MyTest(unittest.TestCase):
	def test_bi_to_dec(self):
		self.assertEqual(11, bi_to_dec(1011))
		self.assertEqual(89, bi_to_dec(1011001))
		self.assertEqual(371, bi_to_dec(101110011))
		self.assertEqual(0, bi_to_dec(0))
		self.assertEqual(1, bi_to_dec(1))

if __name__ == '__main__':
	unittest.main()








