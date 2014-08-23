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
* created by: `frozenset(["same", "as", "sets"])

[examples usage](http://www.codeskulptor.org/#user37_F54mjdc1kz_3.py)

***