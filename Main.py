import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

a = {}
worstTime = {}
medianTime = {}
GraphStuff = [i for i in range(10, 10020, 10)]

def find(n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1

def fillArr(numOfEl):
    a.clear()
    for i in range(numOfEl):
        a[i] = random.randint(0, 1000000)

for i in range(10, 10020, 10):
    fillArr(i)
    worstTime[i] = (timeit.timeit(lambda:find(10000000), number = 10)) / 10

for i in range(10, 10020, 10):
    fillArr(i)
    medianTime[i] = timeit.timeit(lambda:find(a[int(random.randint(1, i - 1))]), number = 1)

plt.figure(1)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива')
plt.scatter(GraphStuff, worstTime.values(), s=5)
plt.grid(False)

plt.figure(2)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива')
plt.scatter(GraphStuff, medianTime.values(), s=5)
plt.grid(False)


plt.show()