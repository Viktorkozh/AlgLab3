import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

a = {}
worstTime = {}
medianTime = {}
GraphStuff = [i for i in range(10, 10020, 10)]
StuffForLsmWorst = {}
StuffForLsmMedian = {}

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

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(worstTime.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(worstTime.values()))) # Я без понятия source: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html
print(alpha)

plt.figure(1)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Худший случай)')
plt.scatter(GraphStuff, worstTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(medianTime.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(medianTime.values())))
print(alpha)

plt.figure(2)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Средний случай)')
plt.scatter(GraphStuff, medianTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

plt.show()