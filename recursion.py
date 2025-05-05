from functools import lru_cache
#from linecache import cache
# def fib(n):
#     if n==1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fib(n-1) + fib(n-2)
#
# for i in range(1, 11):
#     print(i, ":", fib(i))
#
# cache = {}
# val: int = 0
# def fibo(n):
#     if n in cache:
#         return cache[n]
#     if n == 1:
#         val = 1
#     elif n==2:
#         val=1
#     elif n>2:
#         val = fibo(n-1)+fibo(n-2)
#
#     cache[n]=val
#     return val
#
# for i in range(1,500):
#     print(f"{i} Term: {fibo(i)}")

# @lru_cache(maxsize=1000)
# def fib3(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n>2:
#         return  fib3(n-1)+fib3(n-2)
# for i in range(1,10000):
#     print(i, ":", fib3(i))

def TowerOfHanoi(n, source, dest, aux):
    if n == 1:
        print("Move disk 1 from source ", source, "to destination rod ",dest)
        return

    TowerOfHanoi(n-1, source, aux, dest)
    print("Move disk ",n," from source, ",source," to destination ", dest)
    TowerOfHanoi(n-1, source, aux, dest)

n=3
TowerOfHanoi(n, "A","B","C")
