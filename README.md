# Learn_python_with_myra

hey there welcome to my notes for the Google IT Automation with Python Professional Certificate course <3
I will be adding to this daily :D

~~~~In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType

~~~~You can get the data type of any object by using the type() function:
~~~~In Python, the data type is set when you assign a value to a variable:

    x = "Hello World"	str	

    x = 20	int	

    x = 20.5	float

    x = 1j	complex	

    x = ["apple", "banana", "cherry"]	list

    x = ("apple", "banana", "cherry")	tuple

    x = range(6)	range	

    x = {"name" : "John", "age" : 36}	dict

    x = {"apple", "banana", "cherry"}	set	

    x = frozenset({"apple", "banana", "cherry"})	frozenset	

    x = True	bool

    x = b"Hello"	bytes	

    x = bytearray(5)	bytearray	

    x = memoryview(bytes(5))	memoryview	

    x = None	NoneType	

~~~~Variables: Names that we give certain values in our programs
    like containers for data

~~~~Assignment: The process of storing a value inside a variable

~~~~Expression: A combination of numbers, symbols, or other variables that produce a result when evaluated.

~~~~Variable naming no-no's
    -no keywords already used in python
    -no spaces
    -starts with a letter or underscore
    -only letters, numbers, & underscores

    python is case sensitive-capitalization matters


~~~~implicit coversion: the interpreter ( virtual machine, meaning that it is software that emulates a physical computer) automatically converts one data type into another.

~~~~explicit conversion: manualy convert from one data type to another by calling the relevant function we want to convert it to.

****What is interpreter and complier in python?
    Interpreter translates just one statement of the program at a time into machine code. Compiler scans the entire program and translates the whole of it into machine code at once. An interpreter takes very less time to analyze the source code.


~~~~return:Returning values-we use the keyword return, to tell python that this is the return value of a function
-when we call the function we store that value in a variable.
the power of the return statement is it allows us to combine calls to functions and more complex operations which makes your code more reusable.
-return keyword in a functiontells the function to pass data back. When we call the function, we can store the returned value in a variable. Functions can return multiple variables. Don't forget! store all returned values in variables. Functions can also return nothing and just exsist. 

****refactoring: re-writing code to be more self documenting.


~~~~// FLOOR DIVISION - double slash operator: a floor division // divides a number and takes the integer part of the division as the result.

****none-a special data type in python used to indicate that things are empty or they returned nothing,


****What are the values passed into functions as input called?
    A parameter is a special kind of variable used in a function to refer to one of the pieces of data provided as input to the function.

****What is the purpose of the def keyword?
The def keyword is used to create, (or define) a function.