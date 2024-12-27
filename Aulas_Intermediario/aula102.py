# Aprendendo sobre count - contador sem fim (itertools)
from itertools import count

c1 = count(step=1, start=1)
r1 = range(0,200,8)

print('c1',hasattr(c1, '__next__'))
print('c1',hasattr(c1, '__next__'))
print('r1',hasattr(c1, '__next__'))
print('r1',hasattr(c1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('range')
for i in r1:
    print(i)