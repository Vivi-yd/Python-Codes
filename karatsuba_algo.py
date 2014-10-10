# The Karatsuba algorithm for multiplication of 2 intergers.
# Using divide and conquer and recursive algo's -- Vivi.

from math import ceil
from random import randrange

def split(num, m):
    """
    a helper function for spliting a number into 2 parts,
    which are the quotient and the remainder of num divided by 10**m
    
    input: an integer, num.
    output: 2 integers splited from num.
    """
    
    split1 = num//(10**m)
    split2 = num%(10**m)
    
    return split1, split2

print split(1234, 2)
print split(45789, 3)

def karat(int1,int2):
    """
    input: 2 intergers int1 and int2.
    output: int1*int2 by Karatsuba algorithm.
    """
    int1_len = len(str(int1))
    int2_len = len(str(int2))
    
    #m is chosen to be half of length of the longer integer.
    m = int(ceil(max(int1_len, int2_len)/2.0))
    
    # define base case (single digit multiplication).
    if int1_len == 1 and int2_len == 1:
        return int1*int2
    
    else:
        # Recursively calculate z0 = a*c, z1 = b *d , z2= (a+c) * (b+d).
        a, b = split(int1, m)
        c, d = split(int2, m)
        
        z0 = karat(a, c)
        z1 = karat(b, d)
        z2 = karat(a + b, c + d) - z1 - z0
        #print "3z's:",z0, z1, z2
        
        ans = z0*(10**(2*m)) + z2*(10**m) + z1
        return ans
     

def karat_test():
    """
    testing karatsuba function by inputting random numbers
    """
    failed = 0
    for trial in range(100):
        x = randrange(100, 10000)
        y = randrange(100, 10000)
        
        if karat(x, y) != x*y:
            failed += 1
            
    if failed > 0:
        print "failed ", str(failed), "cases"
    
    else:
        print "test passed! yay!!"
        
karat_test()   