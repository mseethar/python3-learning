def divide(i, j):
   try:
      x = i / j
   except ZeroDivisionError:
      print('zero division error')
   else:
      return x
   finally:
      print('finally')

divide(2, 1)
divide(2, 0)
divide("2", "1")

