print(__name__)  # Prints the name of the module

import my_module  # This also executes the high level statements in the module

print(my_module.__name__)

import my_module     # Modules once loaded are not loaded again.

import importlib
importlib.reload(my_module)  # This will load the module again

import fibo

fibo.fib(3)
fibo.fib(0)
series = fibo.fib2(5)
print(series)
series = fibo.fib2(0)
print(series)

#fib = fib.fib  # This will eclipse the module fib. So have to move it off
fib2 = fibo.fib2
fib = fibo.fib

fib(7)
print(fib2(9))

import fibo as fibonacci   # The module fibo is bound to the name fibonacci in the current module's symbol table

fibonacci.fib(1200)

from fibo import fib2    # Adds (or imports) the name fib2 into the current modules symbol table

from fibo import fib2 as fibonacci2_func, fib as fibonacci_func

print('fibonacci2_func', fibonacci2_func(500))

from fibo import *   # Adds all names (except those that begin with an _) from fibo into the current modules symbol table directly

# Modules are searched for as described below
# 1. the built-ins are searched first
# 2. The sys.path is seached after
#     The sys.path value is
#         1. The directory of the input script or the current directory if no input script
#         2. The directory list in PYTHONPATH environment variable
#         3. Any installtion dependent defaults

import sys
print(sys.path)
