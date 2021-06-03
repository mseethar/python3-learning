# Define a function that will return an iterator
# The iterator object should have a function __next__

class MyList:
   def __init__(self, l):
      self.data = l

   def __iter__(self):
      self._index = -1
      return self

   def __next__(self):
      if self._index < len(self.data) - 1:
         self._index += 1
         return self.data[self._index]
      else:
         raise StopIteration

ml = MyList([1, 2, 3, 4, 5, 'six', '''sdfsdf
sfsf
sfsdf
sdfsf
sdfsfd'''])

print('Iterating')
for item in ml:
   print('item ->', item)

print('Iterating again')
for item in ml:
   print('item ->', item)

print('Printing with next')
it = iter(ml)
print(next(it))
print(next(it))
print(next(it))

print('Iterating one more time')
for item in ml:
   print('item ->', item)

# Generators. The following is a generator.
# Generator is a function that has an yield statement
def reverse(data):
   for index in range(len(data)-1, -1, -1):
      yield data[index]


for char in reverse('madhusuthanan'):
   print(char, end='')

print('\n')


def reverse_2(data):
   for item in data:
      yield item

for char in reverse_2('madhu seetharam'):
   print(char, end='')

print('\n')

# This is how we implement an iterator without the generator function or expression
class MyOldList:
   def __init__(self, l):
      self.data = l
   def __iter__(self):
      self.count = 0
      return self
   def __next__(self):
      if (self.count < len(self.data)):
         ret = self.data[self.count]
         self.count += 1
         return ret
      else:
         raise StopIteration

ol = MyOldList([1, 'two', 3, 'four', 5, 'six', 7])
for item in ol:
   print(item)

print('Printing after for loop', item)

class MyNewList:
   def __init__(self, l):
      self.data = l
   def __iter__(self):     # Very elegant way of defining an iterator with generator
      for index in range(0, len(self.data)-1 ):
         yield self.data[index]

nl = MyNewList(['one', 'ii', 3, 'iv', 'five', 6])
for item in nl:
   print(item)
  

# generator expressions
# These are like list comprehensions but without the square brackets
sum_of_squares = sum( i*i for i in range(1, 10)) 
print('Sum of squares', sum_of_squares)

x_vector = [10, 20,30]
y_vector = [7, 5, 3]

print('sum(x_vector*y_vector)', sum( x*y for x, y in zip(x_vector, y_vector)))

gpas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

valedictorian = max((gpa, name) for gpa, name in zip(gpas, names))
print('max', valedictorian)
print(max(gpas))
