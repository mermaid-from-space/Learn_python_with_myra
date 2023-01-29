

def greeting(name):
    print("Welcome, " + name)
    print("You are part of " + department)

# variables

# expressions 

# operations 

# functions: print() write text on the screen, type()tells us the certain type of value,
# str() converts number into a string
# >>>greeting("Blake", "IT Support")
# Welcome, Blake
# You are a part of IT Support
# -start a function definition with the def keyword
# -followed by the name we want to give our function
# -after the name we have paramaters...also called arguments, for the function enclosed in 
# parentheses
# -a function can have no parameters, or it can have multiple parameters
# -paramaters allow us to call a function and pass it data
# -the data is available inside the function as variables with the 
# same name as the parameters.
# -colon at the end of the line
# -after colon the function body starts..delimited by indentation

length = 10
width = 2
area = length * width
print(area)

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " +str(sum))
The sum of both areas is : 20.5


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

>>> hours, minutes, seconds = convert_seconds(5000)
>>> print(hours, minutes, seconds)
1 23 20

# refactoring code example*

def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

>>>calculate(5)
78.5

# vs...

def circle_area(radius)
    pi = 3.14
    area = pi *(radius ** 2)
    print(area)

>>>circle_area(5)
78.5

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2*my_trip_km))


# lucky number

def lucky_number(name):
    number = len(name) * 9
    message = "Hello " + name + ", Your lucky number is " + str(number)
    return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))

# function that compares two numbers and returns them in increasing order

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

smaller, bigger = order_numbers(100,99)
print(smaller,bigger)

# conditional block

# The is_positive function should return True if the number received is positive, otherwise it returns None. 
# Can you fill in the gaps to make that happen?

def is_positive(number):
    if number > 0:
        return true


def is_positive(number):
  if number > 0:
    return True
  else:
    return False

# modulo operator

def is_even(number):
    if number % 2 == 0:
        return True
    return False


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


The value of the python expression ((10 >= 5*2) and (10 <= 5*2)) is True

The code will definitely return a Boolean value(True or False).

For the expression to be True , the two statements must be True. The AND gate returns True if the whole statement is True.

(10 >= 5*2) is True because 10 is equals to 5 × 2 = 10.

(10 <= 5*2) is True because 10 is equals to 5 × 2 = 10.

The two statements are True . Therefore,

True and True = True.


def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	return (numerator / denominator) % 1 if denominator else 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


def format_name(first_name, last_name):
	
	string = 'Name: ' + ', '.join([name for name in [last_name, first_name] if name]) if any([last_name, first_name]) else ''
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# learning about while loops

x = 0
while x > 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

# There are two lines in the body of the loop. In the first line, 
# we print a message followed by the current value of x.
#  In the second line, we increment the value of x. 
#  We do this by adding 1 to its current value and assigning it back to x. 
#  So after the first execution of the body of the loop, x will be 1 instead of 0. 
#  Because this is a loop, the computer doesn't just continue executing with the next line in the script.
#   Instead, it loops back around to re-evaluate the condition for the while loop. 
#   And because 1 here is still smaller than 5, it executes the body of the loop again. 
#   It then prints the message and once more increments x by 1. So the x is now 2.
#    The computer will keep doing this until the condition isn't true anymore. 
#    In this example, the condition will be false when x is no longer smaller than 5. 
#    Once the condition is false, the loop finishes, and the next line is executed.
#     And finally, the last line of our code prints the last value of x.

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

# In this example, we start out by initializing a variable called x. 
# In this case, we initialize it with a value of 1. 
# Then, we enter our while loop which checks to see if the value inside of the x variable is less than the parameter n that the function received. 
# If that comparison evaluates to true, then the code inside the while block is executed. 
# Say we pass a value of 5 as a parameter to this function. 
# In the first pass through the loop, x is always equal to 1, so the comparison: 1 smaller than or equal to 5 would be true and we then enter the body of the loop.
#  In the body, we first print a message indicating that the current attempt number and then we increase the value of x by 1. 
#  To increment the number we're using a slightly different expression than before. 
#  x +=1 is a shorthand version of x = x+1. 
#  You can use either expression since they both mean the same thing. 
#  The process continues until the result of the comparison isn't true anymore, which happens when x is bigger than n.

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()

# In this case, the body of the while loop will be executed until the user enters a valid username.

# countdown while loop! 
def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# here is an infinite loop:

while x % 2 == 0:
    x = x / 2

# This cycle will finish for positive and negative values of x. 
# But what would happen if x was zero? 
# The remainder of 0 divided by 2 is 0, so the condition would be true. 
# The result of dividing 0 by 2 would also be zero, so the value of x wouldn't change. 
# This loop would go on forever, and so we'd get an infinite loop. 
# If our code was called with x having the value of zero, the computer would just waste resources doing a division that would never lead to the loop stopping. 
# The program would be stuck in an infinite loop circling background endlessly

if x != 0:
    while x % 2 ==0:
        x = x / 2

# nest this while loop inside an if statement just like this. 
# With this approach, the while loop is executed only when x is not zero. 
# Alternatively, we could add the condition directly to the loop using a logical operator like in this example. 
# This makes sure we only enter the body of the loop for values of x that are both different than zero and even.

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# break keyword example 

while True:
    do_something_cool()
    if user_requested_to_stop():
        break 

# How do you avoid the most common pitfalls when writing while loops? 
# First, remember to initialize your variables, and second, check that your loops won't run forever. 

# make the print_prime_factors function print all the prime factors of a number.
# A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor = factor + 1
    #   could also be typed factor+=1
  return "Done"

print_prime_factors(100)


# `````````````````````````````````````````````````````````````````````````````````````````````````
# answer to: The following code can lead to an infinite loop. 
# Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    if n == 0:
      break
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# ..................................................................

# answer to: Fill in the empty function so that it returns the sum of all the divisors of a number, 
# without including it. 
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
    sum = 0
    x = 1
    if sum == n:
        return sum
    while x < n:
        if n % x == 0:
            sum = sum + x
        x += 1
    # Return the sum of all divisors of n, not including n
    return sum

# ................................................

# ANSWER: The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
# An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
# Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

# .......................................................................

for x in range(5):
    print(x)

# iterate over a list of numbers to calculate the total sum and average

values = [ 23, 52, 59, 37, 48]
sum = 0
length = 0
for values in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

#  Use while loops when you want to repeat an action until a condition changes. 
# Use for loops when there's a sequence of elements that you want to iterate.

# example d* range() function we want to start with 1 and not zero

product = 1
for n in range(1,10):
    product = product * n

print(product)

# FAHRENHEIT TO CELSIUS converstion formula example e* ***********

def to_celsius(x):
    return(x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

# dominoes tile maker f* **********
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


# home and away teams example g* *************************
teams = [ 'Dragons' , 'Wolves' , 'Pandas' , 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# Greet your friends function*******************

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor' , 'Luisa' , 'Jamaal' , 'Eli'])


# MULTIPLES OF A NUMBER
def multiples(x):
    for n in range(100):
        n = (n*x)
        if n <= 100:
            print(n)
print(multiples(7))


# make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number.
#  Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(2,n+1):
        result = result * x
    return result

for n in range(10):
    print(n, factorial(n))


# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for x in range(1,11):
  print(x**3)


# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
#  Remember that 0 is also a multiple of 7.

# def multiples(x):
#     for n in range(100):
#         n = (n*x)
#         if n <=100:
#             print(n)
# print(multiples(7))


for i in range(0,100):
    if i % 7 == 0:
        print(i)

the range function is used to create a series of numbers from a given range.
 Here the range is used to generate numbers from 0 to 100, 
 Here "if" statement is used to distinguish between numbers divisible by 7 and not divisible by 7, 
 and finally the number divisible by 7 is printed.

# Question 5
# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  
# Currently the code will keep executing the function even if it succeeds. 
# Fill in the blank so the code stops trying after the operation succeeded. break was the answer

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

# recursion function example**
def factorial(n):
    print("Factorial called with " + str(n) )
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returing " + str(result) + " for factorial of " + str(n))
    return result


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# *********A recursive function must include a recursive case and base case. 
# The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.
# A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)


# recursive quiz question
def is_power_of(number, base):
  number = number/base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# Question 3
# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
# Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  number = number/base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# Question 4
# The count_users function recursively counts the amount of users that belong to a group in the company system, 
# by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. 
# But it has a bug! Can you spot the problem and fix it?

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)-1
    
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

# Question 5
# Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive 
# numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n < 1:
    return n
  return n + sum_positive_numbers(n-1)
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# ****graded quizz we3k 3

# Fill in the blanks of this code to print out the numbers 1 through 7.
number = 1
while number < 7:
	print(number, end=" ")
	number += 1
print(number)
...............................................................................................................

# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter
....................................................................................................................
# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits.
#  Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n>0):
		count += 1
		n = n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

............................................................................................................
# This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3 

# 2 4 6 

# 3 6 9

def multiplication_table(start, stop):
	for x in range(start, stop + 1):
		for y in range(start, stop + 1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
................................................................................................................

# The counter function counts down from start to stop when start is bigger than stop, 
# and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

.....................................................................................

# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2,
#  up to and including the maximum that's passed into the function. 
#  For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	for x in range(2 , maximum + 1):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

...............................................................................................
# NOT WORKING 
def decade_counter(year):
	while year < 50:
		year += 10
	return year
decade_counter(45)

.............................
# Modify the double_word function so that it returns the same word repeated twice,
# followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.

def double_word(word):
    word = word * 2
    word_length = str(len(word))
    return word + word_length

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


# string indexing
name = "Myra"
print(name[1])
print(name[0])

# string negative index
text = "Random string wih a lot of characters"
print(text[-1])
print(text[-4])





# String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character.

# You can also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, like [2:5]. 

# This range is similar to the range() function we saw previously. It includes the first number, but goes to one less than the last number. For example:

fruit = "Mangosteen"
fruit[1:4]
'ang'

# The slice includes the character at index 1, and excludes the character at index 4. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving the end of the range:

fruit[:5]
'Mango'

# This gave us the characters from the start of the string through index 4, excluding index 5. On the other hand this example gives is the characters including index 5, through the end of the string:

fruit[5:]
'steen'

# You might have noticed that if you put both of those results together, you get the original string back!

fruit[:5] + fruit[5:]
'Mangosteen'

# you have a string with a character that's wrong and you want to fix it.
# We're not changing the underlying string that was assigned to it before. 
# We're assigning a whole new string with different content. 
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
message = "my back hurts"
print(message)
message = "every chair I get sucks"
print(message)

# using the index method! 
word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# Here, it's a conditional that can be either true or false. key word in...
#  It'll be true if the substring is part of the string, and false if it's not.
pets = "Cats & Dogs"
pets.index("&")
pets.index("C")
print(pets.index("a"))
print("Dragons" in pets) 
print("Cats" in pets)

# Imagine that your company has recently moved to using a new domain, 
# but a lot of the company email addresses are still using the old one. 
# You want to write a program that replaces this old domain with the new one in any outdated email addresses.
#  The function to replace the domain would look like this.
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
      index = email.index("@" + old_domain)
      new_email = email[:index] + "@" + new_domain
      return new_email
  return email  

# string methods let you perform transformations or formatting on the string text, like upper, and its opposite, lower. 
# These methods are really useful when you're handling user input. Let's say you wanted to check if the user answered yes to a question. 
# How would you know if the user typed it using upper or lower case?
#  You don't need to, you just transform the answer to the case you want. Like this example.
print("Mountains".upper())
print("Mountains".lower())

answer = 'Yes'
if answer.lower() == "yes":
  print("User said yes")

#  strip() method. This method will get rid of surrounding spaces in the string. 
#  If we ask the user for an answer, we usually don't care about any surrounding spaces. 
#  So it's a good idea to use the strip method to get rid of any white space. 
#  This means that strip doesn't just remove spaces, 
#  it also removes tabs and new line characters, which are all characters we don't usually want in user-provided strings. 
#  There are two more versions of this method, lstrip rstrip, 
#  to get rid of the whitespace characters just to the left or to the right of the string instead of both sides.

print(" yes ".strip())

print(" yes ".lstrip())

print(" yes ".rstrip())

# The method count() returns how many times a given substring appears within a string.
print("The number of ttimes e occurs in this strng is 4".count("e"))


# The method endswith() resturns whether the string ends with a ceratin substring
print("Forest".endswith("rest"))

# The method isnumeric() returns whether the string's made up of just numbers
print("Forest".isnumeric())
print("12345".isnumeric())

#  if we have a string that is numeric, we can use the int() function to convert it to an actual number.
print(int("12345") + int("54321"))

# we can concatenate strings using the plus sign. The join method can also be used for concatenating.
# To use the join method, we have to call it on the string that'll be used for joining. In this case, we're using a string with a space in it. 
# The method receives a list of strings and returns one string with each of the strings joined by the initial string
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))


# The split() method returns a list of all the words in the initial string and it automatically splits by any whitespace. 
# It can optionally take a parameter and split the strings by another character, like a comma or a dot
print("This is another example".split())


# In this example, we have two variables, name and number. We generate a string that has those variables in 
# it by using the curly brackets placeholder to show where the variables should be written. We then pass the variables as a 
# parameter to the format method. 
# See how it doesn't matter that name is a string and number is an integer? 
# The format() method deals with that, so we don't have to
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}")
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3))

# format() method example
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Let's say you want to output the price of an item with and without tax.
# we can make the format function print only two decimals, like this.
# this is an example of formatting expressions

# These expressions are needed when we want to tell Python to format our values in a way that's different from the default. 
# The expression starts with a colon to separate it from the field name that we saw before. After the colon, we write .2f. 
# This means we're going to format a float number and that there should be two digits after the decimal dot. 
# So no matter what the price is, our function always prints two decimals.
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# using format and float to fix the Fahrenheit to Celsius temperature table:
# In the first expression we're saying we want the numbers to be aligned to the right for a total of three spaces. 
# In the second expression we're saying we want the number to always have exactly two decimal places and we want to align it to the right at six spaces. 
# We can use string formatting like this to make the output of our program look nice and also to generate useful logging and debugging messages.
def to_celsius(x):
    return(x-32)*5/9

for x in range(0,101,10):
    # print(x, to_celsius(x))
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


****WEEK 4 PRACTICE QUIZ NOTES strings
#Question 1
# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, 
# omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for string in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if string.replace(" ", ""):
			new_string = string + new_string
			reverse_string = string + reverse_string
	# Compare the strings
	if new_string[::-1] == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True



# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", 
# with Y having only 1 decimal place. 
# For example, convert_distance(12) should return "12 miles equals 19.2 km"
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km



# Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name 
# followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G."


# The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. 
# If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. 
# For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. 
# The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(sentence) - len(old)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


# ***********Lists in Pythonnnnnnnn
# Eventually in your scripts, you want to develop code that manipulates collections of items like a list of strings 
# representing all the file names in a directory or a list of integers representing the size of network packets. 
# This is where the list data type comes in handy. You can think of lists as long boxes with the space inside the box divided up into different slots. 
# Each slot can contain a different value. 
x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))
print("are" in x)
print("Today" in x)
# use square brackets to indicate where the list starts and ends.
print(x[0])
print(x[3])
# As with strings, we can also use indexes to create a slice of the list. For this, we use ranges of two numbers separated by a colon
print(x[1:3])


# The append method adds a new element at the end of the list. It doesn't matter how long the list is.
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
# The insert method takes an index as the first parameter and an element as the second parameter. 
# It adds the element at that index in the list. 
# To add it as the first element, we use index zero and we can use any other number.
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")
print(fruits)
# The remove method removes from the list the first occurrence of the element we pass to it.
fruits.remove("Melon")
print(fruits)
# The pop method returns the element that was removed at the index that was passed.
fruits.pop(3)
print(fruits)
# In the last way to modify the contents of a list is to change an item by assigning something else to that position,
fruits[2] = "Strawberry"
print(fruits)

# *********TUPLES OMG********
# Tuples are sequences of elements of any type that are immutable. We write tuples in parentheses instead of square brackets.
# when using tuples the position of the elements inside the tuple have meaning. 
# Tuples are used for lots of different things in Python. One common example is the return value of functions. 
# When a function returns more than one value, it's actually returning a tuple. Remember the function to convert seconds to hours, 
# minutes, and seconds that we saw a while back? Here just to remind you. 
# This function returns three values. In other words, it returns a tuple of three elements.
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(result)
hours, minutes, seconds = result
print(hours, minutes, seconds)
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

# Let's use tuples to store information about a file: its name, its type and its size in bytes. 
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 
def file_size(file_info):
	name, type, size = file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



# In this code, we're iterating over a list of strings. For each of the strings, we get its length and add it to the total amount of characters. 
# At the end we print the total and the average which we get by dividing the total by the length of the list. 
# You can see we're using the len function twice, once to get the length of the string and then again to get the amount of elements in the list
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}" .format(chars, chars/len(animals)))


# ****enumerate function***
# The enumerate function returns a tuple for each element in the list. 
# The first value in the tuple is the index of the element in the sequence. 
# The second value in the tuple is the element in the sequence. 
winners = ["Ashely", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))


# Say you have a list of tuples containing two strings each. 
# The first string is an email address and the second is the full name of the person with that email address. 
# You want to write a function that creates a new list containing one string per person including their name and the email address 
# between angled brackets. 
# the format usually used in emails like this. So what do we need to do?
def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name,email))
  return result

print(full_emails([("alex@example.com", "Alex Deigo"), ("shay@example.com", "Shay Brandt")]))


# Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is in an even position or an odd position.
def skip_elements(elements):
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# ***LIST COMPREHENSIONS
# List comprehensions: lets us create new lists based on sequences or ranges
multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)
# oooor do this
multiples = [ x*7 for x in range(1,11)]
print(multiples)


# Say we have a list of strings with the names of programming languages like this one, and we want to generate a list of the length of the strings. 
# We could iterate over the list and add them using a pen like we did before. Or we could use a list comprehension like this
languages = ["Python", "Perl", "Ruby", "Go", "Jave", "C"]
lengths = [len(language) for language in languages]
print(lengths)
#  In this case we just want the element x to be a part of the list, 
#  but we only want the numbers where the remainder of the division by 3 is 0. So we add the conditional clause after the range.
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension. 
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.
def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


******practice quiz: lists******

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, 
# we would like to generate a new list called newfilenames, consisting of the new filenames. 
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        filename = filename.replace(".hpp", ".h")
        newfilenames.append(filename)
    else:
        newfilenames.append(filename)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]




# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first 
# character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + "ay"
    say.append(word)
    # Turn the list back into a phrase
  return " ".join(say)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example: 
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.
def octal_to_string(octal):
    result = ''
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, 
# … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence 
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
# should print out: Ken is 30 years old and works as Chef. 
# Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. 
# Fill in the gaps in this function to do that.
def guest_list(guests):
	for guest in guests:
		name, age, prof = guest
		print("{} is {} years old and works as {}".format(name, age, prof))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer" 



# **********************************dictionaries!!!!! 

# Like lists, dictionaries are used to organize elements into collections. 
# Unlike lists, you don't access elements inside dictionaries using their position. 
# Instead, the data inside dictionaries take the form of pairs of keys and values. T
# o get a dictionary value we use its corresponding key.

x = {}
print(type(x))

file_counts = {"jpg" :10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
#  When creating the dictionary we use colons and between the key and the value and separate each pair by commas. 
#  In a dictionary, it's perfectly fine to mix and match the data types of keys and values like this and can be very useful.
# Dictionaries are mutable
# To add an entry in a dictionary, just use the square brackets to create the key and assign a new value to it.
file_counts["cfg"] = 8
print(file_counts)
#  we can delete elements from a dictionary with the del keyword by passing the dictionary 
#  and the key to the element as if we were trying to access it.
del file_counts["cfg"]
print(file_counts)


# **********ITERATING OVER THE CONTENTS OF DICYIONARY
# you can use for loops to iterate through the contents of a dictionary.
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)

# So if you use a dictionary in a for loop, the iteration variable will go through the keys in the dictionary. 
# If you want to access the associated values, you can either use the keys as indexes of the dictionary 
# or you can use the items method which returns a tuple for each element in the dictionary
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension" .format(amount, ext))


# -------------------PRACTICE QUESTION------------------------

# Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
# Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))

# Because we know that each key can be present only once, dictionaries are a great tool for counting elements and analyzing frequency. 
# Let's check out a simple example of counting how many times each letter appears in a piece of text.
def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result

print(count_letters("sssss"))
print(count_letters("cyborg"))
print(count_letters("a long strng with a bunch of letters"))

# Practice quiz: Dictionaries
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. 
# Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
			    user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))



# The add_prices function returns the total price of all of the groceries in the  dictionary. 
# Fill in the blanks to complete this function.
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44