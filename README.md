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

OPERATORS:

In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False. 

To check if two values are the same, we can use the equality operator: == 

To check if two values are not the same, we can use the not equals operator: != 

We can also check if values are greater than or lesser than each other using > and <. If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError. 

We can make very complex comparisons by joining statements together using logical operators with our comparison operators. These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. When using the or operator, if either side of the comparison is true, then the whole statement is true. Lastly, the not operator simply inverts the value of the statement immediately following it. So if a statement evaluates to True, and we put the not operator in front of it, it would become False.

IF ELSE statements and MODULO

 if statement, which executes code if an evaluation is true and skips the code if it’s false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be executed if the above if statement doesn’t execute.

 modulo operator, which is represented by the percent sign: %. This operator performs integer division, but only returns the remainder of this division operation. If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.

 ELIF 
 Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!

~~~~CONDITIONALS CHEAT SHEET
In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks. 

It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance. 

Comparison operators
a == b: a is equal to b

a != b: a is different than b

a < b: a is smaller than b

a <= b: a is smaller or equal to b

a > b: a is bigger than b

a >= b: a is bigger or equal to b

Logical operators
a and b: True if both a and b are True. False otherwise.

a or b: True if either a or b or both are True. False if both are False.

not a: True if a is False, False if a is True.

Branching blocks

In Python, we branch our code using if, else and elif. This is the branching syntax:

if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block


Remember: The if-block will be executed if condition1 is True. The elif-block will be executed if condition1 is False and condition2 is True. The else block will be executed when all the specified conditions are false.
