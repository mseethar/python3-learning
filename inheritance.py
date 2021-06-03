class A:
   def __init__(self, n):
      self.count = n

   def count_up(self):
      self.count += 1
      return self.count

class B(A):
   def __init__(self, n, m):
      A.__init__(self, n)
      self.step = m

   def count_up(self):
      A.count_up(self)    # We are calling a method defined in a super class
      self.count += self.step
      return self.count

objA = A(20)
print(objA.count_up())
print(objA.count_up())
print(objA.count)
print('isinstance(objA, A)', isinstance(objA, A))
print('issubclass(A, object)', issubclass(A, object))
print('issubclass(A, A)', issubclass(A, A))
print('issubclass(object, A)', issubclass(object, A))

objB = B(40, 2)
print(objB.count_up())
print(objB.count_up())
print(objB.count)
print('isinstance(objB, B)', isinstance(objB, B))
print('isinstance(objB, A)', isinstance(objB, A))
print('isinstance(objA, B)', isinstance(objA, B))
print('issubclass(B, A)', issubclass(B, A))
print('issubclass(A, B)', issubclass(A, B))
print('issubclass(B, object)', issubclass(B, object))
print('issubclass(object, B)', issubclass(object, B))
print('issubclass(B, B)', issubclass(B, B))
