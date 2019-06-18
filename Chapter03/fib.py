import os

limit = int(os.environ['FIB_LIMIT'])
a = 0
b = 1
print(a)
while b < limit:
    print(b)
    b = a + b
    a = b - a