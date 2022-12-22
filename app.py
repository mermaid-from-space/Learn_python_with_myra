# variables

# expressions 

# operations 

# functions: print() write text on the screen, type()tells us the certain type of value,
# str() converts number into a string

def greeting(name):
    print("Welcome, " + name)
    print("You are part of " + department)

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