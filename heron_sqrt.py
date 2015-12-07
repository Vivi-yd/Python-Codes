# heron's method of finding sqrt

from math import fabs

def heron(num):
    
    """
    input: a positive number num (int or float).
    output: the positive squareroot of the number num.
    
    """
    assert(num >= 0 and (type(num) is int or type(num) is float)), "input must be a positive number"
    
    #start the first guess as halve of num
    guess = num/2.0
    
    # this is the tolerance error that is acceptable (accuracy).
    # the lower the number, the more accurate it is.
    epsilon = 0.01
    
    
    # while error is larger than epsilon the function continue 
    #will repeat the loop
    while fabs(num-guess**2) > epsilon:
        
        guess = (guess+num/guess)/2.0
        
    return guess

print heron(16)
print heron(50)
print heron(0)