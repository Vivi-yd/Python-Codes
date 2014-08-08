#Notes here --: 

***

##<week_1>

####Designing Programs:

1. Read - Gather information about the problem from various information sources.
	* Read the problem definition / statement. Discuss the assignment with those who created it and your peers.
	* Gather examples of sample input and desired output.
	* Identify properties of the problem input. Understand and formulate properties of the output.
	* Read the documentation for any APIs/classes provided for the problem.
	
	
2. Think - Consider how to go about solving the problem.
	* Identify what you do and don't understand about solving the problem.
	* Focus on learning how to solve those parts that you don't understand. Read books, articles, forums, Stack Overflow, etc.
	* Experiment in isolation with solutions to parts of the problem that you don't understand.
	* Sketch a step-by-step solution to the problem in English. Refine this solution until you are confident that you understand all of the steps.
	  
3. Sketch - Outline the structure and functionality of your solution.
	* Decide on data representation (*classes*) and algorithms (*methods*) for core computational processes in the solution.
	* Formulate class definitions with needed methods as stubs (using pass or return).
	* Write docstrings for the methods that includes the data types for inputs and outputs.
	
4. Code and test - Implement and test the various methods in your class definitions.
	* Implement the initiailizer method `__init__()` for the class that lays out the basic class data in class fields.
	* Implement the string method `__str__()` method that returns a text representation of the class data.
	* Use the string method to test the initializer on several sets of test data created for the class.
	* For each remaining method, generate example input and output data.
	* Incrementally implement part of each method. Test your partial implementation on the test data. Add more test data as necessary.
	* Repeat this last step as necessary until the implementation is complete. Avoid adding large chunks of code to a method without testing.
	  
5. Review and refactor - Review each version of the solution. Refactor your code to eliminate common issues.
	* Identify repeated code fragments. Introduce appropriate abstractions to remove this duplicated code.
	* Decompose code into smaller logical pieces to avoid lengthy segments of code.
	* Think more and rewrite to simplify convoluted code.
	* dentify computational bottlenecks via counting and rewrite to improve the performance of slow-running code.
	
  make a list of the steps that you follow when building a program to solve a particular problem. 
  This list doesn't have to be particularly detailed, but should be a starting point

***

##<week_4>

####Generators:

* Is an *Iterator*, where a sequences of value is generated, just like a List, but differ from list in that, the whole
* sequences **DOES NOT** get produced all at once before iteration starts to initiate, rather, the value gets produce as iteration progresses.

* Generator Expression (*do not confuse with List Comprehension*):

**A list comprehension** : `print "max in list:", max([num * 2 - 3 for num in range(7)])` 
* This expression generates a list before getting feed into the "max" function.

**A generator expression** : `print "max in gen:", max(num * 2 - 3 for num in range(7))` 
* in this case "max" function takes in a value whenever it gets generated, not taking the whole list.

* Generator Function: contains the `yeild`, which unlike `return`, do not ends the function, but instead, gives or *yeild* a value and continue to run the function until is told to stop.
	
* However, Generator Function **CAN** contain `return` in order to stop the program.


####Stacks and Queues:

Types of data structure (e.g. Class defining) that restrict the way data getting extracted, following **LIFO** for Stack and **FIFO** for Queues.
	
####Inheritance:

* Subclass inherits methods from Baseclass, multiple subclasses can inherits from the same base.
* Methods that got redefined in subclasses will Overwrite the methods with the same names from base.
	
**syntax for defining a subclass that inherits from a baseclass named Base**: `class Sub(Base):`
	

####Duck Typing:

* A way of variables handling used in some languagues such as python, that many others do not, like Java.
* In language that uses duck typing, types of variables are not explicitly defined, thus a program will not consider whether a method is suitable to be called on the variable before executing to ensure correct behavior, rather it will throw errors when execution fails.

*"When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck"*
	

####Search method:
	
* BFS: where an initial point is chosen, and the search spread outward in all directions, checking whether the neighbor of those searched cells are searched and update accordingly.
	
* DFS: where an initial point is given, and the search begin the search unidirectionally until deadend is reached, then change another direction to continue.

***

##<week_5>

####Recursion:

* Define a function and then call itself with less (smaller) data set after each successive calls.
* It is used to solve problem which consists of smaller sub-problem with similar characteristics.
	* First a base case (can be solved easily at once) is identified and defied
	* Then Recursive or Inductive steps are defined to aid the solving of problem by repetive calls to that step.
		

* If a recursive function is designed so that each invocation of the body makes at most one new recursive call, this is known as linear recursion. (The second fib function which I wrote is an example) . The binary search code too is linear. 

* A recursion is a tail recursion if any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing recursion. By necessity, a tail recursion must be a linear recursion. (In the binary search method we have used tail recursion) . 

* **Traditional**: recursive function calls all of the recursive steps before computing the result at the end 
and return the answer right after that computation.

* **Tail recursion**: computes the result before proceeding into the next recursive step, the input of the next 
recursive step is being updated, and thus keeping of previous operations is not required. 


####Recurrence:

* An equation that defines a sequences recursively, when 1 or more base value given initially, all subsequent terms is defined as a function of the preceding terms.

* A closed form solution provides a single function of n that approximate a recurrence relation to produce the nth term of the sequences but eliminate the recursive component of the function.	

####Reading File:

* Reading off network, will need urllib2 or codeskuptor module and call it as in [this example](http://www.codeskulptor.org/#examples_files.py)

* Reading off hard-drive will need to provide the FULL path of the file location to the window and assigned it as file_name, then call: 
`open(file_name, ‘r’)`
`r` for read, `w` for write.

* After opening there are 4 ways to read: `file_name.readline() #print lines with new line (\n) spaces.`
	
	```
	>>>for line in file_name:
		print line  #print the whole file

	>>>print(file_name.read()) #whole file in a single string. (including  the newline character (\n))

	>>>file_name.readlines() #list of all the lines (including  the newline character (\n))
	
	```
