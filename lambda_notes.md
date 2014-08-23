#Lambda function, Map, Filter and Reduce in Python,

### Lambda function:
+ small anonymous function intended to be used on spot, not to keep for future use.
+ can be assigned to a variable to give a name. 
+ format: `func = lambda list_of_arguments : arithmetic expression`
+ can be used in combination with **Map**, **Filter** as well as **Reduce**.

#### Map:
+ map is a method that return a new list after applying the given function to every element of a sequence.
+ map takes `(function, sequence)`
+ Used with lambda: `func = map(lambda_function, seq)`
``` example:
one_to_10 = range(1, 11)
fifth_power = map(lambda x: x**5, seq)
print fifth_power
```
+ map can be applied to more than one sequence of SAME LENGTH
``` example:
mass = [1, 2, 3, 4, 5]
height = [10, 20, 30, 40, 100]

# calculating the potential energy of given mass at given height
E_p = map(lambda m, h: m*h*9.8, mass, height)
print E_p
```

#### Filter:
+ filter returns a list of element that are `True` according to the statement defined in the function after evaluation. 
+ filter takes `(function that returns T/F, list)`
+ Used with lambda: `func = filter(lambda_function, seq)
``` example:
weight_in_lb = [1/3, 1, 2, 3, 4, 5, 10, 100]

# return a list of weight greater than 2kg
two_kg_up = filter(lambda lb : lb/2.2 > 2.0, weight_in_lb)

# return a list of weight smaller than 1kg
one_kg_down = filter(lambda lb : lb/2.2 < 1.0, weight_in_lb)

print two_kg_up
print one_kg_down
>>> [5, 10, 100]
>>>[0, 1, 2]
```

#### Reduce:
+ reduce continually apply the function to the sequence and return a single value. 
+ reduce takes (function, seq)
+ For a seq `[s1, s2, s3, s4...]` then reduce does this: `func(func(func(s1, s2), s3), s4)..`
+ Used with lambda: `func = reduce(lambda_function, seq)
``` example:
lst1 = range(1, 6)
lst2 = range(1, 11)
factorial_five = reduce(lambda m, n: m*n, lst1)
factorial_ten = reduce(lambda m, n: m*n, lst2)

print factorial_five
print factorial_ten
>>> 120
>>> 3628800
```
***
[link](http://www.codeskulptor.org/#user37_uqxl5pJ3Zh_4.py) 

