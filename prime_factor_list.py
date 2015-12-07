from random import randint

def is_prime(n):

	"""
	this function determine whether or not the given number is a prime number

	Input: integer n.
	Output: Booleen (True or False)
	"""
	#by definition
	if n < 2:
		return False


	i = 2 

	while i*i <= n: 
		if n % i == 0:
			return False
		i += 1	

	return True

# for i in range(0, 14):
# 	print str(i), is_prime(i)

		


def prime_factor(n):
	"""
	this function list out all the prime factors of a given number.

	Input: an integer n.
	Output: a list of integers (prime_factor of n).

	"""

	prime_factor = []

	i = 2 #initializing first prime factors

	while i <= n:
		if is_prime(i) == True and n % i == 0:
			n = n/i
			
			prime_factor.append(i)
		i += 1
		
	return prime_factor	



for i in range(50, 61):
	print str(i), prime_factor(i)

			

