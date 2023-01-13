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


The ability to accurately perform repetitive tasks and never get tired is why computers are so great for automation. The automated task could be anything like copying files to a bunch of computers on a network, sending personalized emails to a list of users, or verifying that a process is still running. It doesn't matter how complex the task is, your computer will do it as many times as you tell it to.


while loops
for loops 
recursion

while loops: instruct your computer to continuously execute your code based on the value of a condition.

initializing: To give value to a varable

~~~~ANATOMY OF A WHILE LOOP 

A while loop will continuously execute code depending on the value of a condition. 
It begins with the keyword while, followed by a comparison to be evaluated, then a colon.
 On the next line is the code block to be executed, indented to the right.
  Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. 
  What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. 
  Once the statement is no longer true, the loop exits and the next line of code will be executed.  

  Infinite loop: A loop that keeps executing and never stops.

   BREAK: In Python, we use the break keyword which you can see here to signal that the current loop should stop running. We can use it not only to stop infinite loops but also to stop a loop early if the code has already achieved what's needed


***for Loop : iterates over a sequence of values

in Python and a lot of other programming languages, a range of number will start with the value 0 by default.

the list of numbers generated will be one less thatn the given value.

the power of the for loop is that we can use it to iterate over a sequence of values of any type, not just a range of numbers

*****as an IT specialist, you'll use for loops to automate tons of stuff. For example, you might use them to copy files to machines, process the contents of files, automatically install software, and a lot more.

Use for loops when there's a sequence of elements that you want to iterate.
 Use while loops when you want to repeat an action until a condition changes. 

RECAPPPPPPPPPPPPPPPPPPPP
For loops allow you to iterate over a sequence of values. Let's take the example from the beginning of the video:

for x in range(5):

  print(x)

Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line. Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over. In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.

Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4. Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence. So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.

The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.

Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. A for loop works well when you want to iterate over a sequence of elements.  


*** The range() function ------------------------------

the range function, and how it generates a sequence of numbers starting with zero. Sometimes, though, we don't want to start with zero. For these situations, the range function also allows us to specify the first element of the list to generate. We do that by passing two parameters to the function instead of one, like in the next example d*

Notice that we're using 101 for the upper limit instead of 100. We're doing this because the range never includes the last element, and we want to include 100 in our range. example e*



Previously we had used the range() function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. But the range() function can do much more than that. We can pass in two parameters: the first specifying our starting point, the second specifying the end point. Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified.

The range() function can take a third parameter, too. This third parameter lets you  alter the size of each step. So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5.

To quickly recap the range() function when passing one, two, or three parameters:

One parameter will create a sequence, one-by-one, from zero to one less than the parameter.

Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.

Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.

~~~example f* dominoes tile maker:
In this code, we're using a new parameter that we passed to the print function. This parameter is called end=" ". Normally, once print has taken the content we passed and written it to the screen, then it writes a special character that creates a new line called the newline character. If we want print to write something else instead of the newline character, we use the end=" "


~~~~~~example g* write a script that will output all possible team pairings. For this, the order of the names matters because for each game, the first name will be the home team and the second name is the away team. Of course, what we don't want to do is have a team playing against itself. So what statement do we need to use to avoid that?


LOOPS CHEAT SHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEET~~~~~~~~~~~~~~~~~
Loops Cheat Sheet
Check out below for a run down of the syntax for while loops and for loops.

While Loops
A while loop executes the body of the loop while the condition remains True.

Syntax:

12
while condition:
    body
Things to watch out for!

Failure to initialize variables. Make sure all the variables used in the loop’s condition  are initialized before the loop.

Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables.

 Typical use:

While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

For Loops
A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence.

Syntax:
for variable in sequence:
    body


The range() function:

range() generates a sequence of integer numbers. It can take one, two, or three parameters:

range(n): 0, 1, 2, ... n-1

range(x,y): x, x+1, x+2, ... y-1

range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)

Common pitfalls:

Forgetting that the upper limit of a range() isn’t included.

Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter, but that might not be what you want.

Typical use:

For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

Break & Continue
You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.

You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.



***********RECURSION***************
Recursion is the repeated application of the same procedure to a smaller problem.
Russian nesting doll? They are a great visual example of recursion. Each doll has a smaller doll inside it. 
When you open up the doll to find the smaller one inside, you keep going until you reach the smallest doll which can't be opened.

Recursion lets us tackle complex problems by reducing the problem to a simpler one.

in programming, recursion is a way of doing a repetitive task by having a function call itself. 
A recursive function calls itself usually with a modified parameter until it reaches a specific condition. 
This condition is called the base case.

 In Python by default, you can call a recursive function 1,000 times until you reach the limit. 

******week 4*****
 Data Types and Data Structures
Strings: data type that is used to represent a peice of text. Written between qoutes 'string' + "string"

 we can also access a slice of a string. A slice is the portion of a string that can contain more than one character, also sometimes called a substring. We do that by creating a range using a colon as a separator.
 The range we use when accessing a slice of a string works just like the one created by the range function.

 strings in python are immutable- they can't be modified.