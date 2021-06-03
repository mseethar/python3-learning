# Variables scopes
for m in range(10):
   n = m + 12
   print(m)

print(m)   # m is still accessible outside of the for loop
print(n)   # Even n is accessible here ( that is outside on the for loop)

with open('io.py', 'r') as f:
   print('there are', len(f.readlines()), 'lines in the file')

print(f)    # f is accessible here.
print(f.closed)    # This will be true because the io.TextIOWrapper has predefined Cleanup actions

