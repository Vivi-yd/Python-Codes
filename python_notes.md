#Python notes (self study from various sources)

## Sets and Frozen sets

####Sets:
* A set is a collection of elements with the following characteristics:
	* Unordered.
	* No duplications.
	* Elements cannot be mutable.
	* But the set itself **is** mutable.
	* Can be created by: `set(["elements", "goes", "here"])`
	* Various methods can be used on sets such as add, remove, differences, union..etc

####Frozen Sets:
* Same as sets but **Immutabe**, which means cannot be change but methods like union..etc stil can be used.
* created by: `frozenset(["same", "as", "sets"])`

[examples usage](http://www.codeskulptor.org/#user37_F54mjdc1kz_3.py)

***

####Generators:
* A mechanism which `yield` value one at a time and give as the it runs. Contrast to function where only a single value is `return` and terminates at once.
* An iterator object can be created and called like a function to that object. Where `next()` is a method to obtain the next value in the generator.


* After the generator exhausted all values, it terminates and can not be furthered called.
* To reuse the generator, a **new** object has to be created.

```
# examples:
>>>def five():
>>>    for num in range(5):
>>>            yield num

# create an object
>>>obj = five()

# calling next() to the object 
>>>for itr in range(5):
>>>    print obj.next()

0
1
2
3
4

# recreate object to use again
obj2 = five()

first_three_num = [obj2.next() for itr in range(3)]
print "first three numbers", first_three_num

```

[link to usages]{http://www.codeskulptor.org/#user37_6HslelpZNN_3.py)
[more usage by Ashu](http://www.codeskulptor.org/#user37_Ds2edZ2yft_1.py)

***
