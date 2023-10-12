import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

a = {}
worstTime = {}
medianTime = {}
GraphStuff = [i for i in range(10, 10010, 10)]
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

for i in range(10, 10010, 10):
    fillArr(i)
    worstTime[i] = (timeit.timeit(lambda:find(10000000), number = 100)) / 100

for i in range(10, 10010, 10):
    fillArr(i)
    t = int(random.randint(1, i - 1))
    medianTime[i] = timeit.timeit(lambda:find(a[t]), number = 100) / 100

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(worstTime.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(worstTime.values()))) # Взято из книги "Python Programming And Numerical Methods: A Guide For Engineers And Scientists": https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html

plt.figure(1).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Худший случай)')
plt.scatter(GraphStuff, worstTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

formatted_alpha = [format(a, '.10f') for a in alpha]
print('Коэффициенты прямой худшего случая: a =', formatted_alpha[0], 'b =', formatted_alpha[1])
print('Worst time correlation', np.corrcoef(GraphStuff, list(worstTime.values()))[0, 1])

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(medianTime.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(medianTime.values())))

plt.figure(2).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Средний случай)')
plt.scatter(GraphStuff, medianTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

formatted_alpha = [format(a, '.10f') for a in alpha]
print('Коэффициенты прямой среднего случая: a =', formatted_alpha[0], 'b =', formatted_alpha[1])
print('Median time correlation', np.corrcoef(GraphStuff, list(medianTime.values()))[0, 1])

plt.show()