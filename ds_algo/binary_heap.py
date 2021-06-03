'''Based on complete binary tree. 
Complete binary tree is perfectly balanced, except for the bottom level'''

capacity = 5
N = 0
pq = [-1]

def swap(i, j):
   pq[i], pq[j] = pq[j], pq[i]

def less(i, j):
   return pq[i] < pq[j]

def swim(k):
   while(k//2 >= 1):
      j = k//2
      if(less(k, j)): break
      swap(j, k)
      k = j

def sink(k):
   global N
   while(2*k <= N):
      j = 2 * k
      if(j < N and less(j, j+1)): j += 1
      if(less(j, k)): break
      swap(k, j)
      k = j

def insert(element):
   global N
   pq.append(element)
   N += 1
   swim(N)

def del_max():
   global N
   r = pq[1]
   swap(1, N)
   del pq[N]
   N -= 1
   sink(1)
   return r

f = open('data.txt', 'r')
while line := f.readline():
   insert(int(line))
   if( N > capacity):
      del_max()

print(pq)
