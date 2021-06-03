class A:
   pass

class B(A):
   pass

class C(B):
   pass

class D(B, A):
   pass

print(D.__mro__)    # Prints the method resolution order

print(D.__bases__)  # Prints the base classes tuple in the order that this class extends them
