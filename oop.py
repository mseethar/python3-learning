class MyClass(object):
   common = 10
   _my_private = 2304
   def __init__(self):
      self.myvariable = 3
   def myfunction(self, arg1=None, arg2=None):
      print(self._my_private)
      self._my_private += 1
      return self.myvariable

def printall():
   print(f'myobj1.common: {myobj1.common}')
   print(f'myobj2.common: {myobj2.common}')
   print(f'MyClass.common: {MyClass.common}')
   print(f'myobj1.myvariable: {myobj1.myvariable}')


# Instantiate the classes (create new objects)
myobj1 = MyClass()

myobj2 = MyClass()
printall()

MyClass.common = 20
printall()

myobj1.common = 23
printall()

MyClass.common = 50
printall()

myobj1.myfunction()
myobj2.myfunction()
myobj1.myfunction()
myobj2.myfunction()

print(myobj2._my_private)

class MySubClass(MyClass):
   def __init__(self):
      pass
   def mynewfunction(self):
      return ('a', 1, 3, 4, 4.5)

sub_obj = MySubClass()
sub_obj2 = MySubClass()

(a, b, c, d, e) = sub_obj.mynewfunction()
print(f'a: {a}, b: {b}, c: {c}, d: {d}, e: {e}')

print('defining new attribute newinstvar in sub_obj')
sub_obj.newinstvar = 12         # Adding a new attribute to this instance alone
print('sub_obj.newinstvar', sub_obj.newinstvar)
#print(sub_obj2.newinstvar)       # ERROR: AttributeError: 'MySubClass' object has no attribute 'newinstvar'
del sub_obj.newinstvar     # INFO: object attributes can also be deleted
# print(sub_obj.newvar)      # ERROR: AttributeError: 'MySubClass' object has no attribute 'newvar'

print('defining new attribute newclassvar in MySubClass')
MySubClass.newclassvar = 23     # Attributes can be added at the class level. They will be shared among the instances
print('MySubClass.newclassvar', MySubClass.newclassvar)
print('sub_obj.newclassvar', sub_obj.newclassvar)
print('sub_obj2.newclassvar', sub_obj2.newclassvar)

print('Changing sub_obj.newclassvar = 4')
sub_obj.newclassvar = 4
print('MySubClass.newclassvar', MySubClass.newclassvar)
print('sub_obj.newclassvar', sub_obj.newclassvar)
print('sub_obj2.newclassvar', sub_obj2.newclassvar)

print('changing MySubClass.newclassvar = 29')
MySubClass.newclassvar = 29
print('MySubClass.newclassvar', MySubClass.newclassvar)
print('sub_obj.newclassvar', sub_obj.newclassvar)
print('sub_obj2.newclassvar', sub_obj2.newclassvar)

print('changing sub_obj.newclassvar = 1978 and sub_obj2.newclassvar = 1980') 
sub_obj.newclassvar = 1978
sub_obj2.newclassvar = 1980
print('MySubClass.newclassvar', MySubClass.newclassvar)
print('sub_obj.newclassvar', sub_obj.newclassvar)
print('sub_obj2.newclassvar', sub_obj2.newclassvar)

print('changing MySubClass.newclassvar = 5')
MySubClass.newclassvar = 5
print('MySubClass.newclassvar', MySubClass.newclassvar)
print('sub_obj.newclassvar', sub_obj.newclassvar)
print('sub_obj2.newclassvar', sub_obj2.newclassvar)



class SuperClass:
   number_of_sides = 4      # Class variable
   def __init__(self, l, w):
      self._length = l       # Instance variable
      self._width = w
   def area(self):
      # Instance variables cannot be referenced without the self reference
      # print('length is', length)   # ERROR: NameError: name 'length' is not defined
      return self.length() * self.width()
   def length(self, length):
      self._length = length
   def width(self, width):
      self._width = width
   def length(self):     # Python has no overloading. Methods cannot differ only in number or type of arguments
      return self._length
   def width(self):
      return self._width

obj1 = SuperClass(2, 5)

# SuperClass.length()    # This is a function object
# obj1.length()    # This is a method object

print(obj1.length)
print(obj1.width)
print(obj1.area())

print(obj1.length())
print(obj1.width())
#obj1.length(3)   # ERROR: TypeError: length() takes 1 positional argument but 2 were given
#obj1.width(7)

print(obj1.length())
print(obj1.width())
print(obj1.area())
print(dir(SuperClass))


class VarAndFunctionInSameScope:
   def __init__(self):
      self.add_temp = 5    #NOTE: All the instance variables and methods MUST be referred by the self
   def change(self):
      self.add = 53
   # The function attribute is the object is overridden by the initializer
   # It adds a data attribute with the same name as that of the function
   def add(self):
      #change()      # NameError: name 'change' is not defined
      self.change()  # Calling this method causes the add function attribute to be changed as a instance data attribute
      return 5 + 7

print(dir(VarAndFunctionInSameScope))
print('type(VarAndFunctionInSameScope.add)', type(VarAndFunctionInSameScope.add))

obj3 = VarAndFunctionInSameScope()
print('type(obj3.add)', type(obj3.add))
print('type(VarAndFunctionInSameScope.add)', type(VarAndFunctionInSameScope.add))
print(obj3.add)

print(dir(obj3))
print(obj3.add())

#print(obj3.add())  # TypeError: 'int' object is not callable


# Defining class functions outside of a class
def f1(self, i, j):
   self.i = i
   self.j = j
   return i + j

class C:
   f = f1   # Assigning the function object to the local variable of the class object is ok
   def __init__(self):
      self.i = 0
      self.j = 0

class D:
   def __init__(self):
      pass
   def d_func(self):
      return f1(self, 3, 4)   # INFO Referring a global function

d = D()
print(d.d_func())

print(d.__class__)  # prints <class '__main__.D'>
print(dir(d.__class__))
five = 5
print(five.__class__)

class E(int):
  pass

print(dir(E))


class X:
   def __init__(self, num):
      self.data = num

class Y(X):
   def __init__(self, another_num):
      self.data = another_num

x = X(3)
y = Y(30)

print(x.data)
print(y.data)

print(isinstance(x, X))
print(isinstance(x, (X, Y)))
print(isinstance(x, Y))
print(isinstance(y, X))

