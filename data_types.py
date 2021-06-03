print(2 + 3)
print (2/3)   # Not an integer division

try:
   print(a)  # a is not defined yet. So it will throw NameError: name 'a' is not defined
except NameError:
   print('NameError exception is thrown')
else:
   print('NameError is not thrown')
finally:
   print('Executing finally')

print( 5 ** 2)   # power operator. this is 5 squared
print(2 ** 8)    # 2 to the power 8

#print(_)    # ERROR: _ is not defined

print('Py'   'thon')   # two or more adjacent strings are automatically concatenated

# Breaking long strings
long_string = ('This is such a long string that you may want to break it '
               'so that you avoid scroll blindness for you and others, '
               'otherwise it will be hard for someone to read and understand '
               'constantly scrolling through the source code editor')

print(long_string)

