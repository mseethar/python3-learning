import sys

print(type(sys.argv))   # This is a list
# The first argument is the name of the script file
print(sys.argv[0])   # Arguments to the command line are available in sys.argv variable
if len(sys.argv) > 1:
   print(f'There were {len(sys.argv)} arguments provided: {sys.argv}')

sys.argv.append('12312')  #System arguments list is mutable
print(sys.argv)

''' This is a multiline string.
It can also be used as a multi-line comment'''

hello = "hello"
hello += " world!!!"

print(hello)

one = "1"
two = "2"

print(one + " " + two)
one, two = two, one
print(one + " " + two)

# DONT name a variable list. It is a builtin name
listobj = [1, 2, "three", [4, "five"], 6, {"seven": 7, 8: "eight"}, (9, 10, "eleven")]
#listobj.remove(3)   #INFO: remove() doesn't work by index but by value
listobj.remove(listobj[2])

print('listobj', listobj)

print(listobj[0])
print(listobj[-1])

# DONT name a variable map. It is a builtin name
mapobj = {"one": 1, 2: "two", "iii": "three", 4: ("IV", "iv", 4, "four") }
print(mapobj["one"])
print(mapobj[2])

#print(mapobj["1"]) #Throws KeyError 

print(len(mapobj))

length = len           # Aliasing a function

print(length(listobj))

tuple_of_tuple = (1, 2, 4, (5, 6, 7, 8) )

print(tuple_of_tuple)

print(len(tuple_of_tuple))
print(tuple_of_tuple[-1])      # tuple's elements can also be accessed by index

print(hello[3:])     # Accessing range

print(hello[::2])    # The third argument is for stepping two items at a time

print(hello[-3:-1])   # From last to third from last

# Strings

string1 = 'Hello world!'        # Strings can either be single quoted
string2 = "Hello world!"        # or double quoted
string3 = 'He said "Hi!"'       # A single quoted string can have double quotes inside, in any number
string4 = "What does 'lol' stand for?"   # A double quoted string can have single quotes inside, any numbers
string5 = '''Multi-lin
strings
are
here'''                        # Multi-line strings can either be single quoted
string6 = """Another multi-line
string is here!
Did you notice?

"""                            # or double quoted
string6 = r'\\d\\r\n'    # The leading r in defining the string, prevents the backslashes being escaped
print(string6)
#Python Strings are always unicode
#bytestrings can be defined as below
bytestring = b'Hello \xce\xb1'    # class bytes
print(bytestring)
print(type(bytestring))

print(b'Hello \xce\xb1')
print(bytestring.decode('utf-16'))

bytestring_converted_to_string = bytestring.decode('utf-16')     # class str
print(type(bytestring_converted_to_string))

# string substitution with tuples
print("This %s a %s" % ('is', 'test'))
#print("Random %s of %s" % ('number'))  #ERROR: TypeError: not enough arguments for format string
print("String substitution with %s type mismatch" % (23))
# too many arguments than required by the format method
# print("String substitution with %d type match" % (23, 43))    #ERROR: TypeError: not all arguments converted during string formatting

# string substitution with dictionary
print("This %(verb)s a %(noun)s" % {'noun': 'test', 'verb': 'is'})

# The substitution operator is equivalent to the format method in string
print("substitute %s %s function".format(('with', 'the')))

# Variable substitution
name = 'Madhu'
greeting = 'Hello {} very {} ok? {}'.format(name, 'good morning', 23)
print(greeting)
print(f'{name} is good and his greeting is {greeting}')    # NOTE: Please note the f in front of the string

# The {} placeholder works only with the format method. It does not work with the % operator
#greeting = 'Hello {} vary {}' % (name, 'evening')    #ERROR: TypeError: not all arguments converted during string formatting
#print(greeting)

# Control statements if, for , while
import random    # Import a module
randint = random.randint(0, 99)    # Gives a random integer between 0 and 99 inclusive
is_even = False
if randint % 2 == 0:
   print(f'We got an even number: {randint}')
   is_even = True
else:
   print(f'We got an odd number: {randint}')
rng = range(100)   # ranges include the beginning index and excludes the end index
print(rng)

for n in rng:
   if is_even:
      print('Breaking the for loop because the random number is even')
      break
# for and while loops can have an else clause as well.
# This will be executed when the for loop is not broken (with a break statement), that is it completes fully
else:
   print('for loop is not broken because the random number was odd')

rangelist = list(range(10))
print(f'rangelist: {rangelist}')
if rangelist[3] == 3:
   print('this is false. lists are index 0 based')
elif randomlist[3] == 4:
   print('this is true')
else:
   print('something')

count = 0
while count < 100:
   #print(count)
   count += 1

#count++         # NOTE: There is no increment ++ or decrement -- operator in python. This line does not compile
print(++count)   # NOTE: This line compiles because it is an unary operator. This translates to +(+count)
print(--count)
print(-+count)
print(+-count)

# Functions
increment = lambda x: x + 1
print(increment(9))

# Optional args are assigned a value
def myfunction(a_list, an_int, another_int=4, a_string='Whatever'):
   a_list.append('EOL')
   an_int = 7636
   return a_list, an_int, another_int, a_string

my_list = [1, 2, 3, 4, 5]
my_int = 10

print(f'Original passed values: my_list {my_list}, my_int: {my_int}')
(ret_list, ret_int, ret_another_int, ret_a_string) = myfunction(my_list, my_int)

print(f're_list: {ret_list}, ret_int: {ret_int}, ret_another_int: {ret_another_int}, ret_a_string: {ret_a_string}')
# List is mutable. So it will be changed after the function call.
# int and string are immutable. So they remain the same.
print(f'Original passed values after call: my_list: {my_list}, my_int: {my_int}')

print(myfunction(an_int=43, a_list=my_list))   # Calling a function with named arguments

from random import randint  # Import a function directly
newrandint = randint(0, 1)
# Exceptions handling
try:
   10 / newrandint
except ZeroDivisionError:
   # When there is a ZeroDivisionError this code handles that
   print('Zero division error')
else:
   # If there was no exception thrown above, the following snippet is executed
   print('No zero division error')
finally:
   # This code is executed always, whether there was an exception or not
   # This gets executed even if there were further exception in the handler
   print('finally')

import random
#from time import clock

def func1():
   # print(globalvar)  # ERROR: UnboundLocalError: local variable 'globalvar' referenced before assignment
   globalvar = 'Hey'
   print(globalvar)

def func2():
   global globalvar
   print(globalvar)
   globalvar = 'Howdy'

globalvar = "Hello"
func1()
print(globalvar)
func2()
print(globalvar)

# List comprehensions
# Expression followed by a for and followed by zero or more if and for clauses
list1 = [1, 2, 3]
list2 = [3, 4, 5]

new_list = [ i * j for i in list1 for j in list2]
print(f'new_list: {new_list}')
new_generator = ( i + j for i in list1 for j in list2 )  # This is not a tuple but a generator (expression) object 
print(f'new_generator: {new_generator}')
print(new_generator)

generated_list = list(new_generator)   # Create a list using the generator
print(generated_list)
print(type(generated_list))

sum_int = sum( 1 for i in [3, 3, 4, 5, 6, 3, 4] if i == 4 )   # Sums the items of a list
print(sum_int)

print(any([ i % 3 for i in [1, 3, 3, 4, 5, 6,7 ]]))   # Prints True if any of the number in the list is not divisible by 3

del list1[1]  # Removes the second element from the list
print(list1)

del list1    # Removes the variable list1 altogether
#print(list1)   # ERROR: NameError: name 'list1' is not defined

'''Even if the lists are of different lengths the zip will combine them
upto the smallest array's length'''

list1 = ['Madhu', 'Ladha', 'Akshitha', 'Akshath']
list2 = [42, 40, 12, 8, 40]   # NOTE: There are 5 elements in this array
list3 = ['Vanilla', 'Strawberry', 'Chocolate', 'Mango', 'Orange', 'Fruity']   # 6 elements

print(zip(list1, list2, list3))  #zip function returns a zip object

print('zipping lists')
for i in zip(list1, list2, list3):
   print(type(i))
   print(i)
   print('{} is {} years old and likes {} icecream'.format(*i))
   # ^ format method takes positional parameters. So we have to spread the tuple if we want to use it here
   # If we don't spread ERROR: IndexError: Replacement index 1 out of range for positional args tuple

print('zipping list of lists')
for i in zip(*[list1, list2, list3]):
   print(type(i))
   print(i)
   print('{} is {} years old and likes {} icecream'.format(*i))

# COUNTING
ratings = [ random.randint(1, 10) for _ in range(1, 1001) ]
#print(ratings)

for i in range(1, 11):
   print('{} occurs {} times'.format(i, ratings.count(i)))

print(sum(ratings.count(i) for i in range(1, 11)))

ratings_count = [(i, ratings.count(i)) for i in range(1, 11)]  # Creating a tuple of the number and its count in the list
print(ratings_count)

# If we don't know the values in the list, we add them in a set
unique_values = set(ratings)

for i in unique_values:
   print('{} occurs {} times'.format(i, ratings.count(i)))

print('Counting with the counter object')
from collections import Counter
# Using Counter class
counter = Counter(ratings)

for rating in counter:
   print('{} occurs {} times'.format(rating, counter[rating]))

print('Printing 3 most common')
for rating_tup in counter.most_common(3):
   print('{} occurs {} times'.format(*rating_tup))   # The * here is called parameter expansion

# Enumerating
names = ['James', 'John', 'Dan', 'Dale', 'Jim', 'Dave']

for i in range(len(names)):
   print('{}: {}'.format(i+1, names[i]))

for i, name in enumerate(names, 1):
   print('{}: {}'.format(i, name))

# Parameter expansion
def print_personal_info(name, age, company, designation):
   print(f'name: {name}, age: {age}, company: {company}, designation: {designation}')

personal_info = ['Madhu', 42, 'PayPal', 'Sr. MTS']
print_personal_info(*personal_info)

ages = [21, 34, 27, 42, 26, 32]
companies = ['Facebook', 'Amazon', 'Netflix', 'Google', 'Microsoft', 'Cisco']
designations = ['Associate', 'Sr. Developer', 'Lead', 'MTS', 'MTS-2', 'Architect']

personal_information = zip(names, ages, companies, designations)

for info in personal_information:
   print_personal_info(*info)
   #personal_info_map = map()    # We cannot create a map like this as map() is a built-in function https://docs.python.org/3/library/functions.html
   personal_info_dict = {}    # Empty map creation
   (personal_info_dict['name'], personal_info_dict['age'], personal_info_dict['company'], personal_info_dict['designation']) = info
   print(personal_info_dict)
   print_personal_info(**personal_info_dict)  # map / dictionary parameter expansion. This is equivalent to named arguments passing

# Type annotations
def mul(i, j):
   return i * j

# Both the above and below are valid. But the type annotated below one is better in documentation
# Please note that Python does not check any types. We can pass anything (int or not).
def multiply(i: int, j: int):
   return i * j

print(multiply(names, 3))

# Exception handling
try:
   x = x / 0
except NameError:
   print('x is not defined yet. So NameError is thrown')
else:
   print('NameError is not thrown.')
finally:
   print('This will be executed whether or not an exception is thrown')

try:
   x = 5 / 0
except ZeroDivisionError:
   print('ZeroDivisionError is thrown')
else:
   print('ZeroDivisionError is not thrown')
finally:
   print('finally')

try:
   y = 's' + 5
except TypeError:
   print('TypeError is thrown')
else:
   print('TypeError is not thrown')
finally:
   print('TypeError finally')

class BException(Exception):
   pass

class CException(BException):
   pass

class DException(CException):
   pass

for cls in [BException, CException, DException]:
   try:
      raise cls()    # Creating an object of the exception class and throwing it
   except DException:
      print('DEx thrown')   # A child class's except can catch only itself and not it's parent's
   except CException:
      print('CEx thrown')
   except BException:      # A base class's except clause can catch itself and any of its sub classes
      print('BEx thrown')
   else:
      print('BEx is not thrown')

def handle_exception():
   print('Unknown Ex: ', sys.exc_info()[0])     # The details of the exception that is being handled by this thread can be
   # retrieved by this function
   exc_type, exc_value, exc_traceback = sys.exc_info()
   print('exc_type', exc_type, 'exc_value', exc_value, 'exc_traceback', exc_traceback)
   for excp in sys.exc_info():      #  AttributeError: module 'sys' has no attribute 'exe_info'
      print(type(excp))
      print('is_none: ', excp == None, excp)

try:
   raise(TypeError, 'I am throwing a custom TypeError')
except:        # A wildcard except clause
   handle_exception()

#if __name__ == '__main__':
#   raise TypeError


# Tuple packing and unpacking
a = 1
b = 3

a, b = b, a    # On the right a tuple is packed (created). On the left the tuple is unpacked
print(f'a is {a} and b is {b}')

#Variables can also be unpacked from lists
my_list = ['Madhu', 42, 'NoWhen']
name, age, whence = my_list
print(f'name is {name}, age is {age} and whence is {whence}')

#my_list.append('Srivi')
#name1, age1, whence1 = my_list  # ValueError: too many values to unpack (expected 3)
#print('name1', name1, 'age1', age1, 'whence1', whence1)

my_list2 = [my_list, ['German', 1000, 'Germany']]

print(my_list2)
for name, age, when in my_list2:
   print(name, age, when)

leading_except_last_three, (name, age, whence) = my_list2

print(leading_except_last_three, name, age, whence)

string_1 = 'abrakadabraopensesame'

print(' '.join(string_1))   # Joins a list or iterable with the string in between

print(list(enumerate(my_list)))  #  [(0, 'Madhu'), (1, 42), (2, 'NoWhen')]
print(my_list.index(42))  # 1

for (a, b) in list(enumerate(my_list)):
   print(a, b)

my_list = [[(1, 2, 3), (2, 3, 4)], [(4, 5, 6), (5, 6, 7)]]

for ((a, b, c), (d, e, f)) in my_list:
   print(a, b, c, d, e, f)

for [[a, b, c], [d, e, f]] in my_list:
   print(a, b, c, d, e, f)

for ([a, b, c], (d, e, f)) in my_list:
   print(a, b, c, d, e, f)

my_list1 = my_list[:]

print(my_list1 == my_list)
