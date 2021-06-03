
def try1():
   try:
      x = 5 / 0
   except ZeroDivisionError as ex:
      raise RuntimeError('Something bad1 happened') from ex   # Chaining the exception directly.
      # This iexception object is added to the __cause__ variable

def try2():
   try:
      x = 4 / 0
   except ZeroDivisionError:
      raise RuntimeError('Somthing bad2 happened')   
      # The ZeroDivisionError object is added to the __context__ of this RuntimeError

def try2_1():
   try:
      x = 4 / 0
   finally:
      raise RuntimeError('Somthing bad2_1 happened')
      # The ZeroDivisionError object is added to the __context__ of this RuntimeError

def try2_2():
   try:
      x = 4 / 0
   except ZeroDivisionError:
      raise RuntimeError('Something bad bad happened')
   finally:
      raise RuntimeError('Somthing bad2_2 happened')
      # The ZeroDivisionError object is added to the __context__ of this RuntimeError

def try3():
   try:
      x = 3 / 0
   except ZeroDivisionError:
      print('Doing nothing')
   finally:
      raise RuntimeError('Something bad3 happened')
      # The ZeroDivisionError object is added to the __context__ of this RuntimeError

def try4():
   try:
      x = 2 / 0
   except:
      raise RuntimeError('Somthing bad4 happened') from None
      # Breaking the default chaining behavior

#try1()       # The above exception was the direct cause of the following exception
#try2()     # During handling of the above exception, another exception occurred:
#try2_1()  # During handling of the above exception, another exception occurred:
try2_2()   # During handling of the above exception, another exception occurred:   - twice
#try3()    # No chaining or association in context
#try4()    # No chaining or association in context
