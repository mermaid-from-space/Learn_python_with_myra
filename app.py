

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