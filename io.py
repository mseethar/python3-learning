def pt(some_object):
   print(type(some_object))

   print(some_object)

import pickle

# WRITE BINARY
file1 = open('./out/my-list-serialized.out', 'wb')   # If we do not specify the b it throws TypeError: write() argument must be str, not bytes
pt(file1)
my_list = [1, '23', 'four', 78]
pickle.dump(my_list, file1)
file1.close()
print(f'Initial list: {my_list}')

# READ BINARY
file1 = open('./out/my-list-serialized.out', 'rb')
pt(file1)
loaded_list = pickle.load(file1)
file1.close()
print(f'Loaded list: {loaded_list}')

file2 = open('./out/mytext.txt', 'w')
pt(file2)
file2.write('This is a castle')
file2.close()

file2 = open('./out/mytext.txt')   # By default files are read in READ mode
pt(file2)
str_read = file2.read()
pt(str_read)
file2.close()

print(str_read)

# Predefined cleanup actions

with open('io.py') as f:
   print('there are', len(f.readlines()), 'lines in the file')

print(f)
