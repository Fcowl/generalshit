import timeit
from functools import cache,lru_cache

import sys
sys.setrecursionlimit(2000)
@lru_cache(maxsize=None)
def f1(n):
    if n < 10:
        return 1
    return (n+3)*f1(n-3)

@cache
def f2(n):
    if n < 10:
        return 1
    return (n+3)*f2(n-3)

def test1():
    a = (f1(x) for x in range(1, 247563))
    print(  (f1(247563)/519-477*f1(247560))/f1(247557)  )

def test2():
    a = (f2(x) for x in range(1, 247563))
    print((f2(247563) / 519 - 477 * f2(247560)) / f2(247557))

#t1 = timeit.timeit(lambda :test1(), number=10)
#t2 = timeit.timeit(lambda :test2(), number=10)
test1()

#print(t1, t2)
