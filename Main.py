import timeit
import random

a = {}
med = 0

def find(n):
    Found = 0
    for i in range(len(a)):
        if a[i] == n:
            Found = 1
            return i
    if Found == 0:
        return -1

def fillArr(numOfEl):
    for i in range(numOfEl):
        a[i] = random.randint(0, 1000000)

num = 100000
fillArr(num)

worstTime = timeit.timeit(lambda:find(12212100), number = 1000) / 1000
print('Average worst case:', worstTime)