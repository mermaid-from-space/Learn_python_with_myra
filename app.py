

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

# The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?

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