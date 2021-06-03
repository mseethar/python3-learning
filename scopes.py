def scope_test():
   def do_local():
      spam = 'local spam'

   def do_nonlocal():
      nonlocal spam
      spam = 'nonlocal spam'

   def do_global():
      global spam
      spam = 'global spam'

   spam = 'test spam'
   do_local()
   print(spam)
   do_nonlocal()
   print(spam)
   do_global()
   print(spam)
   # Let me define a class in the local scope
   class ThisIsMyClass:
      pass
   class ThisIsMyGlobalClass:
      pass
   global ThisIsMyGlobalClassOut    # If we want to export this class to the module scope
   ThisIsMyGlobalClassOut = ThisIsMyGlobalClass
   class MyClass2:
      ''' This is the doc string'''
      def static_method():
         print('I am a static method')
      def instance_method(self):
         print('I am an instance method')
   import __main__        # This is another way to export a class to the main module's (script's) scope
   __main__.MyClass2 = MyClass2

scope_test()
print('In global', spam)

#This class is defined inside a function and is out of scope in the global namespace
#obj1 = ThisIsMyClass()    # ERROR: NameError: name 'ThisIsMyClass' is not defined

obj2 = ThisIsMyGlobalClassOut()      # ThisIsMyGlobalClass is aliased to a global name ThisIsMyGlobalClassOut at #26

obj3 = MyClass2()    # MyClass2 is added as an attribute to the module in #30

MyClass2.myvar = 23

print(obj3.myvar)
print(MyClass2.myvar)
MyClass2.static_method()
# The following method cannot be invoked becasue the method does not have the argument for the object's reference
#obj3.static_method()   #  ERROR:  TypeError: static_method() takes 0 positional arguments but 1 was given
obj3.instance_method()
print(obj3.__doc__)
