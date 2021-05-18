from functools import lru_cache
import sys


@lru_cache(maxsize=65)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


sys.setrecursionlimit(100000)
f = int(input("Pls enter fib value: "))
print(fib(f))

print(fib.cache_info())
