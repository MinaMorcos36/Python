x = 5
y = 2
z = int(x/y)
print(z)

y = "Hello World!"
print(y)

# comment

x = str("mmm")
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print(type(z))
print(type(x))

x = "Mina"
# single = double quotes, x != X
X = 'Mina'

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

a, b, c = "Apple", "Banana", "Cherry"
print(a)
print(b)
print(c)

d = e = f = "Fruits"
print(d)
print(e)
print(f)

fruits = ["mango", "grapes", "peach"]
h, y, z = fruits
print(h)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
# notice the spaces in , or +

x = 5
y = 5
print(x + y)

j = 5
k = "Five"
# print(j + k)  # error if +
print(j, k)  # Comma is the best to separate

g = "good"

def myfunc():
    print("Python is " + g)
myfunc()

x = "awesome"

def thisfun():
    x = "fantastic"
    print("Python is " + x)
thisfun()
print("Python is " + x)

def anotherfun():
    global x
    x = "really good"
    print("Python is " + x)

anotherfun()
print("Python is " + x)

x = range(6)
print(x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(z)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# or 3 single quotes

a = "Hello, World!"
print(a[0])
print(a[1], a[2])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)  # Case Sens

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])  # 5 not included and index is 0
print(b[:5])  # slice from first
print(b[2:])  # slice to end

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a)
print(a.strip())  # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("l", "J"))

a = "Hello, World!"
print(a.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Code	Result
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

z = 9 ** 2  # ** expo
print(z)

z = 9 // 2  # // floor div
print(z)

a = 3
b = 5
if b > a:
    print("b is greater than a")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("a is greater than b")

a = 400
b = 4
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:  # same as or and not
  print("Both conditions are True")

a = 33
b = 200

if b > a:
  pass

mlist1 = ["abc", 34, True, 40, "male"]
for x in mlist1:
 print(type(x))

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
