import timeit
import random

a = {}
med = 0
worstTime = {}
medianTime = {}
j = 0

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

for i in range(10, 10020, 10):
    fillArr(i)
    worstTime[j] = (timeit.timeit(lambda:find(1232121121), number = 10)) / 10
    j += 1

print(worstTime)

j = 0
for i in range(10, 10020, 10):
    med = 0
    fillArr(i)
    for h in range(100):
        med += timeit.timeit(lambda:find(a[int(random.randint(i - 1 // 2 - int(i * 0.3), i // 2 + int(i * 0.3)))]), number = 1)
    medianTime[j] = med / 100
    j += 1

print('Median:\n', medianTime)