import sys

for arg in sys.argv[1:]:
   try:
      f = open(arg, 'r')
   except OSError as ex:
      print('ERROR  : Cannot open file:', arg)
      print(type(ex))
      print(ex.args)
      print(ex)
   else:
      print('SUCCESS:', arg, 'has', len(f.readlines()), 'lines')   # NOTE: f is visible here
      f.close() 
