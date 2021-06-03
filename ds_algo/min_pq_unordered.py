pq = []
capacity = 5

def append(num):
   #pq[len(pq)] = num   # IndexError: list assignment index out of range
   pq.append(num)

def swap(i, j):
   pq[i], pq[j] = pq[j], pq[i]

def del_max():
   global pq
   max_index = 0
   for i in range(len(pq)):
      if pq[max_index] < pq[i]:
         max_index = i
   swap(max_index, len(pq)-1)
   if len(pq) > capacity:
      del pq[len(pq)-1]
      

f = open('data.txt', 'r')
while line := f.readline():
   append(int(line))
   del_max()

print(pq)
