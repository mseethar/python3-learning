print('Initing the module')

def fib(num):
   a, b = 0, 1
   while(a < num): 
      print(a, end=' ')
      a, b = b, a+b
   print()

def fib2(num):
   fib_list = []
   a, b = 0, 1
   while(a < num):
      fib_list.append(a)
      a, b = b, a+b
   return fib_list

def hi():
   print("Hi")

print('Done initing the module')

if __name__ == '__main__':  # If the module is invoked from CLI the name will be assigned to __main__ . It does not run if the module is imported
   import sys
   fib(int(sys.argv[1]))
